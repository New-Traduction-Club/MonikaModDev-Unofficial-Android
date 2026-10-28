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

    def masl_show_notification(title, message, image_path=None):
        if renpy.android and PythonActivity.mActivity:
            NotificationWorker.showNotification(
                PythonActivity.mActivity,
                title,
                message,
                image_path
            )

    def masl_schedule_notification(delay_sec, title, message, image_path=None):
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
    
    def masl_state_day_tl():
        if mas_globals.time_of_day_3state == "morning":
            return "mañana"
        elif mas_globals.time_of_day_3state == "afternoon":
            return "tarde"
        elif mas_globals.time_of_day_3state == "evening":
            return "noche"
        else:
            return "noche"
    
    def masl_state_day_another_dlg_tl():
        if mas_globals.time_of_day_3state == "evening":
            return "esta noche"
        else:
            return "mañana"

init 10 python:
    import store
    # Wrap mas_set_pronouns to automatically update end_letter_gender and pronouns
    if hasattr(store, "mas_set_pronouns"):
        _old_mas_set_pronouns = store.mas_set_pronouns

        MAS_PRONOUN_GENDER_MAP_ES = {
            "hero": {"M": "héroe", "F": "heroína", "X": "héroe"},
            "bf": {"M": "novio", "F": "novia", "X": "pareja"},
            "boy": {"M": "chico", "F": "chica", "X": "persona"},
            "guy": {"M": "chico", "F": "chica", "X": "persona"},
            "man": {"M": "hombre", "F": "mujer", "X": "persona"},
            "him": {"M": "él", "F": "ella", "X": "ellos"},
            "himself": {"M": "él mismo", "F": "ella misma", "X": "sí mismos"},
            "he": {"M": "él", "F": "ella", "X": "ellos"},
            "his": {"M": "su", "F": "su", "X": "su"},
            "hes": {"M": "él es", "F": "ella es", "X": "ellos son"},
            "heis": {"M": "él es", "F": "ella es", "X": "ellos son"}
        }

        def mas_set_pronouns(key=None):
            _old_mas_set_pronouns(key)
            masl_set_end_letter_gender(key)

            if getattr(store.persistent, "language", None) == "spanish":
                if key is None:
                    key = getattr(store.persistent, "gender", "X")
                for word, sub_map in MAS_PRONOUN_GENDER_MAP_ES.items():
                    val = sub_map.get(key, sub_map.get("X"))
                    setattr(store, word, val)

        store.mas_set_pronouns = mas_set_pronouns

        mas_set_pronouns()
