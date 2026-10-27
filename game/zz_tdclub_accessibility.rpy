default persistent._masl_android_menu_enabled = True
default persistent._masl_fontsize_dialogue = 24
default persistent._masl_fontsize_name = 24
default persistent._masl_fontsize_choice = 24
default persistent._masl_scrollbar_size = 18

init -1 python:
    MASL_FONT_SIZE_MIN = 18
    MASL_FONT_SIZE_MAX = 32
    MASL_FONT_SIZE_STEP = 1

    MASL_FONT_SIZE_DIALOGUE_DEFAULT = 24
    MASL_FONT_SIZE_NAME_DEFAULT = 24
    MASL_FONT_SIZE_CHOICE_DEFAULT = 24

    MASL_SCROLLBAR_SIZE_MIN = 12
    MASL_SCROLLBAR_SIZE_MAX = 36
    MASL_SCROLLBAR_SIZE_STEP = 2
    MASL_SCROLLBAR_SIZE_DEFAULT = 18

    def masl_apply_font_sizes(rebuild=True):
        """
        Applies customized font sizes to dialogue, namebox, and choice button styles.

        IN:
            rebuild - True if style.rebuild() should be called, False otherwise.
                (Default: True)
        """
        dialogue_sz = getattr(persistent, "_masl_fontsize_dialogue", None) or MASL_FONT_SIZE_DIALOGUE_DEFAULT
        name_sz = getattr(persistent, "_masl_fontsize_name", None) or MASL_FONT_SIZE_NAME_DEFAULT
        choice_sz = getattr(persistent, "_masl_fontsize_choice", None) or MASL_FONT_SIZE_CHOICE_DEFAULT

        gui.text_size = dialogue_sz
        gui.name_text_size = name_sz
        gui.choice_button_text_size = choice_sz

        dialogue_styles = (
            "say_dialogue", "normal", "default_monika",
            "edited", "edited_dark", "say_thought"
        )
        for s_name in dialogue_styles:
            if hasattr(style, s_name):
                getattr(style, s_name).size = dialogue_sz

        name_styles = ("say_label", "say_label_dark")
        for s_name in name_styles:
            if hasattr(style, s_name):
                getattr(style, s_name).size = name_sz

        choice_styles = (
            "choice_button_text", "choice_button_text_dark",
            "talk_choice_button_text", "talk_choice_button_text_dark",
            "scrollable_menu_button_text", "scrollable_menu_button_text_dark",
            "twopane_scrollable_menu_button_text", "twopane_scrollable_menu_button_text_dark",
            "generic_button_text_base"
        )
        for s_name in choice_styles:
            if hasattr(style, s_name):
                getattr(style, s_name).size = choice_sz

        if rebuild:
            style.rebuild()

    def masl_apply_scrollbar_size(rebuild=True):
        """
        Applies customized scrollbar sizes to vertical and horizontal scrollbar styles.

        IN:
            rebuild - True if style.rebuild() should be called, False otherwise.
                (Default: True)
        """
        scrollbar_sz = getattr(persistent, "_masl_scrollbar_size", None) or MASL_SCROLLBAR_SIZE_DEFAULT

        gui.scrollbar_size = scrollbar_sz

        vscrollbar_styles = (
            "vscrollbar", "vscrollbar_dark",
            "classroom_vscrollbar", "classroom_vscrollbar_dark",
            "game_menu_vscrollbar"
        )
        for s_name in vscrollbar_styles:
            if hasattr(style, s_name):
                getattr(style, s_name).xsize = scrollbar_sz

        hscrollbar_styles = (
            "scrollbar", "scrollbar_dark"
        )
        for s_name in hscrollbar_styles:
            if hasattr(style, s_name):
                getattr(style, s_name).ysize = scrollbar_sz

        if rebuild:
            style.rebuild()

    def masl_adjust_font_size(target, delta):
        """
        Adjusts target font size by delta, clamped between min and max boundaries.

        IN:
            target - string identifier for target font ("dialogue", "name", or "choice")
            delta - integer amount to adjust size by
        """
        if target == "dialogue":
            val = (getattr(persistent, "_masl_fontsize_dialogue", None) or MASL_FONT_SIZE_DIALOGUE_DEFAULT) + delta
            persistent._masl_fontsize_dialogue = max(MASL_FONT_SIZE_MIN, min(MASL_FONT_SIZE_MAX, val))
        elif target == "name":
            val = (getattr(persistent, "_masl_fontsize_name", None) or MASL_FONT_SIZE_NAME_DEFAULT) + delta
            persistent._masl_fontsize_name = max(MASL_FONT_SIZE_MIN, min(MASL_FONT_SIZE_MAX, val))
        elif target == "choice":
            val = (getattr(persistent, "_masl_fontsize_choice", None) or MASL_FONT_SIZE_CHOICE_DEFAULT) + delta
            persistent._masl_fontsize_choice = max(MASL_FONT_SIZE_MIN, min(MASL_FONT_SIZE_MAX, val))

        masl_apply_font_sizes(rebuild=True)
        renpy.restart_interaction()

    def masl_reset_font_size(target):
        """
        Resets target font size(s) back to default value(s).

        IN:
            target - string identifier for target font to reset ("dialogue", "name", "choice", or "all")
        """
        if target in ("dialogue", "all"):
            persistent._masl_fontsize_dialogue = MASL_FONT_SIZE_DIALOGUE_DEFAULT
        if target in ("name", "all"):
            persistent._masl_fontsize_name = MASL_FONT_SIZE_NAME_DEFAULT
        if target in ("choice", "all"):
            persistent._masl_fontsize_choice = MASL_FONT_SIZE_CHOICE_DEFAULT
        if target == "all":
            persistent._masl_scrollbar_size = MASL_SCROLLBAR_SIZE_DEFAULT
            masl_apply_scrollbar_size(rebuild=False)

        masl_apply_font_sizes(rebuild=True)
        renpy.restart_interaction()

    def masl_adjust_scrollbar_size(delta):
        """
        Adjusts scrollbar size by delta, clamped between min and max boundaries.

        IN:
            delta - integer amount to adjust size by
        """
        val = (getattr(persistent, "_masl_scrollbar_size", None) or MASL_SCROLLBAR_SIZE_DEFAULT) + delta
        persistent._masl_scrollbar_size = max(MASL_SCROLLBAR_SIZE_MIN, min(MASL_SCROLLBAR_SIZE_MAX, val))

        masl_apply_scrollbar_size(rebuild=True)
        renpy.restart_interaction()

    def masl_reset_scrollbar_size():
        """
        Resets scrollbar size back to default value.
        """
        persistent._masl_scrollbar_size = MASL_SCROLLBAR_SIZE_DEFAULT

        masl_apply_scrollbar_size(rebuild=True)
        renpy.restart_interaction()

init 1000 python:
    masl_apply_font_sizes(rebuild=False)
    masl_apply_scrollbar_size(rebuild=False)

screen accessibility():

    tag menu

    use game_menu(_("Accessibility"), scroll="viewporty0"):

        vbox:
            xoffset 50
            spacing 20

            if renpy.android:
                vbox:
                    style_prefix "generic_fancy_check"
                    label _("Android Settings")

                    textbutton _("Android Menu"):
                        action ToggleField(persistent, "_masl_android_menu_enabled")
                        selected persistent._masl_android_menu_enabled

                null height (gui.pref_spacing)

            vbox:
                spacing 14

                label _("Font Sizes")

                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text _("Dialogue Text"):
                            font gui.interface_font
                            size 18
                            color gui.interface_text_color
                            yalign 0.5
                        text _("(Default: 24px)"):
                            font gui.interface_font
                            size 14
                            color ("#888888" if not mas_globals.dark_mode else "#aaaaaa")
                            outlines []
                            yalign 0.5

                    hbox:
                        spacing 8
                        yalign 0.5

                        textbutton "-":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_font_size, "dialogue", -MASL_FONT_SIZE_STEP)
                            sensitive (persistent._masl_fontsize_dialogue > MASL_FONT_SIZE_MIN)

                        frame:
                            xsize 80
                            ysize 36
                            padding (0, 0)
                            text "[persistent._masl_fontsize_dialogue] px":
                                align (0.5, 0.5)
                                font gui.default_font
                                size 18
                                color ("#000000" if not mas_globals.dark_mode else "#ffffff")
                                outlines []

                        textbutton "+":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_font_size, "dialogue", MASL_FONT_SIZE_STEP)
                            sensitive (persistent._masl_fontsize_dialogue < MASL_FONT_SIZE_MAX)

                        textbutton _("Reset"):
                            style "mas_button_simple"
                            ysize 36
                            action Function(masl_reset_font_size, "dialogue")
                            sensitive (persistent._masl_fontsize_dialogue != MASL_FONT_SIZE_DIALOGUE_DEFAULT)

                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text _("Name / Bold Text"):
                            font gui.interface_font
                            size 18
                            color gui.interface_text_color
                            yalign 0.5
                        text _("(Default: 24px)"):
                            font gui.interface_font
                            size 14
                            color ("#888888" if not mas_globals.dark_mode else "#aaaaaa")
                            outlines []
                            yalign 0.5

                    hbox:
                        spacing 8
                        yalign 0.5

                        textbutton "-":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_font_size, "name", -MASL_FONT_SIZE_STEP)
                            sensitive (persistent._masl_fontsize_name > MASL_FONT_SIZE_MIN)

                        frame:
                            xsize 80
                            ysize 36
                            padding (0, 0)
                            text "[persistent._masl_fontsize_name] px":
                                align (0.5, 0.5)
                                font gui.default_font
                                size 18
                                color ("#000000" if not mas_globals.dark_mode else "#ffffff")
                                outlines []

                        textbutton "+":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_font_size, "name", MASL_FONT_SIZE_STEP)
                            sensitive (persistent._masl_fontsize_name < MASL_FONT_SIZE_MAX)

                        textbutton _("Reset"):
                            style "mas_button_simple"
                            ysize 36
                            action Function(masl_reset_font_size, "name")
                            sensitive (persistent._masl_fontsize_name != MASL_FONT_SIZE_NAME_DEFAULT)

                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text _("Choice Buttons"):
                            font gui.interface_font
                            size 18
                            color gui.interface_text_color
                            yalign 0.5
                        text _("(Default: 24px)"):
                            font gui.interface_font
                            size 14
                            color ("#888888" if not mas_globals.dark_mode else "#aaaaaa")
                            outlines []
                            yalign 0.5

                    hbox:
                        spacing 8
                        yalign 0.5

                        textbutton "-":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_font_size, "choice", -MASL_FONT_SIZE_STEP)
                            sensitive (persistent._masl_fontsize_choice > MASL_FONT_SIZE_MIN)

                        frame:
                            xsize 80
                            ysize 36
                            padding (0, 0)
                            text "[persistent._masl_fontsize_choice] px":
                                align (0.5, 0.5)
                                font gui.default_font
                                size 18
                                color ("#000000" if not mas_globals.dark_mode else "#ffffff")
                                outlines []

                        textbutton "+":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_font_size, "choice", MASL_FONT_SIZE_STEP)
                            sensitive (persistent._masl_fontsize_choice < MASL_FONT_SIZE_MAX)

                        textbutton _("Reset"):
                            style "mas_button_simple"
                            ysize 36
                            action Function(masl_reset_font_size, "choice")
                            sensitive (persistent._masl_fontsize_choice != MASL_FONT_SIZE_CHOICE_DEFAULT)

                null height 5

            null height (gui.pref_spacing)

            vbox:
                spacing 14

                label _("Scrollbars")

                vbox:
                    spacing 4
                    hbox:
                        spacing 10
                        text _("Scrollbar Width"):
                            font gui.interface_font
                            size 18
                            color gui.interface_text_color
                            yalign 0.5
                        text _("(Default: 18px)"):
                            font gui.interface_font
                            size 14
                            color ("#888888" if not mas_globals.dark_mode else "#aaaaaa")
                            outlines []
                            yalign 0.5

                    hbox:
                        spacing 8
                        yalign 0.5

                        textbutton "-":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_scrollbar_size, -MASL_SCROLLBAR_SIZE_STEP)
                            sensitive (persistent._masl_scrollbar_size > MASL_SCROLLBAR_SIZE_MIN)

                        frame:
                            xsize 80
                            ysize 36
                            padding (0, 0)
                            text "[persistent._masl_scrollbar_size] px":
                                align (0.5, 0.5)
                                font gui.default_font
                                size 18
                                color ("#000000" if not mas_globals.dark_mode else "#ffffff")
                                outlines []

                        textbutton "+":
                            style "mas_button_simple"
                            xsize 40
                            ysize 36
                            action Function(masl_adjust_scrollbar_size, MASL_SCROLLBAR_SIZE_STEP)
                            sensitive (persistent._masl_scrollbar_size < MASL_SCROLLBAR_SIZE_MAX)

                        textbutton _("Reset"):
                            style "mas_button_simple"
                            ysize 36
                            action Function(masl_reset_scrollbar_size)
                            sensitive (persistent._masl_scrollbar_size != MASL_SCROLLBAR_SIZE_DEFAULT)

            null height 5

            textbutton _("Reset All to Default"):
                style "mas_button_simple"
                action Function(masl_reset_font_size, "all")
                sensitive (persistent._masl_fontsize_dialogue != MASL_FONT_SIZE_DIALOGUE_DEFAULT or persistent._masl_fontsize_name != MASL_FONT_SIZE_NAME_DEFAULT or persistent._masl_fontsize_choice != MASL_FONT_SIZE_CHOICE_DEFAULT or persistent._masl_scrollbar_size != MASL_SCROLLBAR_SIZE_DEFAULT)
