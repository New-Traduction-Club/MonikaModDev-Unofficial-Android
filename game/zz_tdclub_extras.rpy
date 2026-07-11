default persistent.language = None

default end_letter_gender = "o"

init python:

    # current plataform string for spanish use
    cur_plat_es = "ordenador" if not renpy.android else "móvil"

    if renpy.android:
        from jnius import autoclass
        PythonActivity = autoclass("org.renpy.android.PythonSDLActivity")
        NotificationWorker = autoclass("org.renpy.android.NotificationWorker")
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
                piano_manager = autoclass("org.renpy.android.PianoManager")
                getattr(piano_manager, action_name)()
            except Exception:
                pass

    def show_android_piano():
        _run_android_piano_action("showPianoKeyboard")

    def hide_android_piano():
        _run_android_piano_action("hidePianoKeyboard")
