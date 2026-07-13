default persistent.language = None

default end_letter_gender = "o"

init python:

    # current plataform string for spanish use
    cur_plat_es = "ordenador" if not renpy.android else "móvil"

    if renpy.android:
        from jnius import autoclass
        PythonActivity = autoclass(str("org.renpy.android.PythonSDLActivity"))
        NotificationWorker = autoclass(str("org.renpy.android.NotificationWorker"))
    else:
        autoclass = None
        PythonActivity = None
        NotificationWorker = None

    def show_notification(title, message, image_path=None):
        if renpy.android and PythonActivity.mActivity:
            NotificationWorker.showNotification(
                PythonActivity.mActivity,
                title,
                message,
                image_path
            )

    def schedule_notification(delay_sec, title, message, image_path=None):
        if renpy.android and PythonActivity.mActivity:
            NotificationWorker.scheduleNotification(
                PythonActivity.mActivity,
                long(delay_sec),
                title,
                message,
                image_path
            )

    def _run_android_piano_action(action_name):
        if renpy.android:
            try:
                piano_manager = autoclass(str("org.renpy.android.PianoManager"))
                getattr(piano_manager, action_name)()
            except Exception:
                pass

    def show_android_piano():
        _run_android_piano_action("showPianoKeyboard")

    def hide_android_piano():
        _run_android_piano_action("hidePianoKeyboard")

    def masl_set_end_letter_gender(key=None):
        """
        Sets the gender-specific letter ending for Spanish translation.

        IN:
            key - Optional[Literal["M", "F", "X"]] - key (perhaps current gender) to set the letter ending for
                If None, uses persistent.gender
        """
        store = renpy.store

        if key is None:
            key = store.persistent.gender

        if key == "F":
            store.end_letter_gender = "a"
        else:
            store.end_letter_gender = "o"

init 10 python:
    import store
    # Wrap mas_set_pronouns to automatically update end_letter_gender
    if hasattr(store, "mas_set_pronouns"):
        _old_mas_set_pronouns = store.mas_set_pronouns

        def mas_set_pronouns(key=None):
            _old_mas_set_pronouns(key)
            masl_set_end_letter_gender(key)

        store.mas_set_pronouns = mas_set_pronouns
