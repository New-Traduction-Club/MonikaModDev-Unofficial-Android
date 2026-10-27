label android_menu_en:
    menu:
        "Gifts":
            jump giftmenu_en
        "Affect":
            jump affectionmenu_en
        "Changelog":
            jump changelog_en
        "Just's Notes (porter)":
            jump notas_en
        "Nevermind":
            return

label notas_en:
    "Like on the old times..."
    return

label changelog_en:
    "MAS updated to 0.12.19."
    "Added the famous android menu button & accessibility options."
    "Someone really reads this?"
    return

label affectionmenu_en:
    "The affection of [persistent._mas_monika_nickname] is [store._mas_getAffection()] points."
    return

label giftmenu_en:
    menu:
        "Write a Gift":
            call screen give_custom_gift_screen_en
        "Predefined Gifts":
            call giftmenu_predefined_en
        "Dynamic gift menu (All posible sprites)":
            jump giftmenu_dynamic_en
        "Return":
            return
    return

label giftmenu_dynamic_en:
    python:
        from store.mas_sprites_json import giftname_map
        import os

        sorted_giftnames = sorted([
            giftname for giftname in giftname_map.keys()
            if not giftname.startswith("__")
        ])
        items = [
            (giftname + ".gift", giftname + ".gift", False, False)
            for giftname in sorted_giftnames
        ]
        display_area = store.mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA
        scroll_align = store.mas_ui.SCROLLABLE_MENU_XALIGN
        final_item = ("Return", False, False, False, 20)

    call screen mas_gen_scrollable_menu(items, display_area, scroll_align, final_item)
    $ result = _return

    if result and result not in ("Return", "Regresar"):
        python:
            gift_path = os.path.join(renpy.config.basedir, "characters", result)
            if not os.path.exists(gift_path):
                with open(gift_path, "w") as f:
                    f.write("")
        $ give_custom_gift(result)
    return

init python:
    def get_unregifted_gifts():
        from store.mas_sprites_json import giftname_map
        gifted = list(persistent._mas_filereacts_sprite_gifts.keys())
        return [
            g for g in giftname_map.keys()
            if not g.startswith("__") and g not in gifted
        ]

screen dynamic_gift_menu_en():
    tag menu
    vbox:
        spacing 10
        for gift in get_unregifted_gifts():
            textbutton gift.replace(".gift", "") action Function(give_custom_gift, gift)
        textbutton _("Return") action Return()

default gift_input = ""
init python:
    def give_custom_gift(gift_name):
        if gift_name.endswith(".gift") or gift_name.endswith(".txt"):
            filepath = os.path.join(renpy.config.basedir, 'characters', gift_name)
            with open(filepath, "a") as f:
                pass

label giftmenu_predefined_en:
    menu:
        "Ribbon (Bisexual Pride Themed)":
            python:
                gift_input = "bisexualpridethemedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Black and White)":
            python:
                gift_input = "blackandwhiteribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Bronze)":
            python:
                gift_input = "bronzeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Brown)":
            python:
                gift_input = "brownribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gradient)":
            python:
                gift_input = "gradientribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Low-Poly Gradient)":
            python:
                gift_input = "lowpolygradientribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Rainbow Gradient)":
            python:
                gift_input = "rainbowgradientribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (White Polka Dots on Red)":
            python:
                gift_input = "whiteonredpolkadotribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Starry Black Sky)":
            python:
                gift_input = "starryblackskyribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Starry Red Sky)":
            python:
                gift_input = "starryredskyribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Blue and White Stripes)":
            python:
                gift_input = "blueandwhitestripedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pink and White Stripes)":
            python:
                gift_input = "pinkandwhitestripedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Transgender Pride Themed)":
            python:
                gift_input = "transgenderpridethemedribbon.gift"
                give_custom_gift(gift_input)
        "Hairclip (Crescent Moon)":
            python:
                gift_input = "crescentmoonhairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Ghost)":
            python:
                gift_input = "ghosthairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Pumpkin)":
            python:
                gift_input = "pumpkinhairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Bat)":
            python:
                gift_input = "bathairclip.gift"
                give_custom_gift(gift_input)
        "Choker (Chain, Silver)":
            python:
                gift_input = "chokerchainsilver.gift"
                give_custom_gift(gift_input)
        "Choker (Daisy, White)":
            python:
                gift_input = "chokerdaisywhite.gift"
                give_custom_gift(gift_input)
        "Choker (Emerald, Green)":
            python:
                gift_input = "chokeremeraldgreen.gift"
                give_custom_gift(gift_input)
        "Choker (Glitter Bead, Silver)":
            python:
                gift_input = "chokerglitterbeadsilver.gift"
                give_custom_gift(gift_input)
        "Choker (Ribbon, Red)":
            python:
                gift_input = "chokerribbonred.gift"
                give_custom_gift(gift_input)
        "Choker (Ruffles, Red)":
            python:
                gift_input = "chokerrufflesred.gift"
                give_custom_gift(gift_input)
        "Choker (Silk, White)":
            python:
                gift_input = "chokersilkwhite.gift"
                give_custom_gift(gift_input)
        "Choker (Spiked, Star)":
            python:
                gift_input = "chokerspikedstar.gift"
                give_custom_gift(gift_input)
        "Choker (Spiral, Black)":
            python:
                gift_input = "chokerspiralblack.gift"
                give_custom_gift(gift_input)
        "Choker (Thread, Ribbon)":
            python:
                gift_input = "chokerthreadribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Black, mini)":
            python:
                gift_input = "miniblackribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Dark pink, mini)":
            python:
                gift_input = "minidarkpinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gray, mini)":
            python:
                gift_input = "minigrayribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Orange, mini)":
            python:
                gift_input = "miniorangeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pale green, mini)":
            python:
                gift_input = "minipalegreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pink, mini)":
            python:
                gift_input = "minipinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Purple, mini)":
            python:
                gift_input = "minipurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Red, mini)":
            python:
                gift_input = "miniredribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Royal blue, mini)":
            python:
                gift_input = "miniroyalblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Sky blue, mini)":
            python:
                gift_input = "miniskyblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (White, mini)":
            python:
                gift_input = "miniwhiteribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Yellow, mini)":
            python:
                gift_input = "miniyellowribbon.gift"
                give_custom_gift(gift_input)
        "Bralette (Red, Ruffles)":
            python:
                gift_input = "braletteredruffles.gift"
                give_custom_gift(gift_input)
        "Button Up (Flowered)":
            python:
                gift_input = "buttonupflowered.gift"
                give_custom_gift(gift_input)
        "Dress (Dark blue, sparkly)":
            python:
                gift_input = "dressdarkbluesparkle.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Black)":
            python:
                gift_input = "heartcutbikiniblack.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Green)":
            python:
                gift_input = "heartcutbikinigreen.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Pink)":
            python:
                gift_input = "heartcutbikinipink.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Purple)":
            python:
                gift_input = "heartcutbikinipurple.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (White)":
            python:
                gift_input = "heartcutbikiniwhite.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Yellow)":
            python:
                gift_input = "heartcutbikiniyellow.gift"
                give_custom_gift(gift_input)
        "Shuchi'in Academy Uniform":
            python:
                gift_input = "shuchiinacademyuniform.gift"
                give_custom_gift(gift_input)
        "Sleeveless Turtleneck (Black)":
            python:
                gift_input = "sleevelessturtleneckblack.gift"
                give_custom_gift(gift_input)
        "T-Shirt (Jurassic Park)":
            python:
                gift_input = "tshirtjurassicpark.gift"
                give_custom_gift(gift_input)
        "T-Shirt (Jurassic World)":
            python:
                gift_input = "tshirtjurassicworld.gift"
                give_custom_gift(gift_input)
        "V-cut Crossed Straps Tanktop (White)":
            python:
                gift_input = "vcutcrossedstrapstanktopwhite.gift"
                give_custom_gift(gift_input)
        "Pearl earrings":
            python:
                gift_input = "pearlearrings.gift"
                give_custom_gift(gift_input)
        "Piercings (Black-silver)":
            python:
                gift_input = "blacksilverpiercings.gift"
                give_custom_gift(gift_input)
        "Dress (Green)":
            python:
                gift_input = "greendress.gift"
                give_custom_gift(gift_input)
        "Jacket (Brown)":
            python:
                gift_input = "brownwinterjacket.gift"
                give_custom_gift(gift_input)
        "Shirt (Put on a happy face)":
            python:
                gift_input = "putonahappyfaceshirt.gift"
                give_custom_gift(gift_input)
        "Shirt (Blue)":
            python:
                gift_input = "blueshirt.gift"
                give_custom_gift(gift_input)
        "Shirt (Rest Here)":
            python:
                gift_input = "resthereshirt.gift"
                give_custom_gift(gift_input)
        "Sweater Vest (Blue)":
            python:
                gift_input = "bluesweatervest.gift"
                give_custom_gift(gift_input)
        "Tanktop (White)":
            python:
                gift_input = "tanktop.gift"
                give_custom_gift(gift_input)
        "Turtleneck Sweater (Beige)":
            python:
                gift_input = "beigeturtlenecksweater.gift"
                give_custom_gift(gift_input)
        "Hoodie (Green)":
            python:
                gift_input = "greenhoodie.gift"
                give_custom_gift(gift_input)
        "YoRHa No.2 Type B":
            python:
                gift_input = "2bcosplay.gift"
                give_custom_gift(gift_input)
        "Anchor Necklace":
            python:
                gift_input = "anchor_necklace.gift"
                give_custom_gift(gift_input)
        "Animal Crossing Necklace":
            python:
                gift_input = "animalcrossing_necklace.gift"
                give_custom_gift(gift_input)
        "Cactus Necklace":
            python:
                gift_input = "cactus_necklace.gift"
                give_custom_gift(gift_input)
        "Gold Chain Necklace":
            python:
                gift_input = "goldchain_necklace.gift"
                give_custom_gift(gift_input)
        "Snail Shell Necklace":
            python:
                gift_input = "snailshell_necklace.gift"
                give_custom_gift(gift_input)
        "Purple Star Necklace":
            python:
                gift_input = "star_necklace.gift"
                give_custom_gift(gift_input)
        "Sunflower Necklace":
            python:
                gift_input = "sunflower_necklace.gift"
                give_custom_gift(gift_input)
        "Triforce Necklace":
            python:
                gift_input = "triforce_necklace.gift"
                give_custom_gift(gift_input)
        "Hairclip (Cherry)":
            python:
                gift_input = "cherryhairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Heart)":
            python:
                gift_input = "hearthairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (8th Note)":
            python:
                gift_input = "musicnotehairclip.gift"
                give_custom_gift(gift_input)
        "Ribbon (Coffee)":
            python:
                gift_input = "coffeeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gold)":
            python:
                gift_input = "goldribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Hot Pink)":
            python:
                gift_input = "hotpinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Lilac)":
            python:
                gift_input = "lilacribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Lime Green)":
            python:
                gift_input = "limegreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Navy Blue)":
            python:
                gift_input = "navyblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Orange)":
            python:
                gift_input = "orangeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Royal Purple)":
            python:
                gift_input = "royalpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Sky Blue)":
            python:
                gift_input = "skyblueribbon.gift"
                give_custom_gift(gift_input)
        "Kimono (Pink)":
            python:
                gift_input = "pinkkimono.gift"
                give_custom_gift(gift_input)
        "Pullover (Black and White Stripe)":
            python:
                gift_input = "blackandwhitestripedpullover.gift"
                give_custom_gift(gift_input)
        "Bow (Black)":
            python:
                gift_input = "blackbow.gift"
                give_custom_gift(gift_input)
        "Pullover (Wine Asymmetrical)":
            python:
                gift_input = "wineasymmetricalpullover.gift"
                give_custom_gift(gift_input)
        "Flower (Pink)":
            python:
                gift_input = "pinkflower.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Blue)":
            python:
                gift_input = "bluetwinribbon.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Green)":
            python:
                gift_input = "greentwinribbon.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Pink)":
            python:
                gift_input = "pinktwinribbon.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Yellow)":
            python:
                gift_input = "yellowtwinribbon.gift"
                give_custom_gift(gift_input)
        "Bikini (Shell)":
            python:
                gift_input = "shellbikini.gift"
                give_custom_gift(gift_input)
        "Hatsune Miku":
            python:
                gift_input = "hatsunemikucosplay.gift"
                give_custom_gift(gift_input)
        "Sakuya Izayoi":
            python:
                gift_input = "sakuyaizayoicosplay.gift"
                give_custom_gift(gift_input)
        "Sweater (Shoulderless)":
            python:
                gift_input = "shoulderlesssweater.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Blue)":
            python:
                gift_input = "8blueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Emerald)":
            python:
                gift_input = "8emeraldribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit White)":
            python:
                gift_input = "8whiteribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Amdek Amber)":
            python:
                gift_input = "amdekamberribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Game Boy Green)":
            python:
                gift_input = "gameboygreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Purple)":
            python:
                gift_input = "8purpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Red)":
            python:
                gift_input = "8redribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Super Game Boy Green)":
            python:
                gift_input = "supergameboygreenribbon.gift"
                give_custom_gift(gift_input)
        "Heart Choker":
            python:
                gift_input = "heartchoker.gift"
                give_custom_gift(gift_input)
        "Choker (Flowered)":
            python:
                gift_input = "floweredchoker.gift"
                give_custom_gift(gift_input)
        "Choker (Simple)":
            python:
                gift_input = "simplechoker.gift"
                give_custom_gift(gift_input)
        "Bunny Scrunchie (Blue)":
            python:
                gift_input = "bluebunnyscrunchie.gift"
                give_custom_gift(gift_input)
        "Ribbon (Black, s-type)":
            python:
                gift_input = "stypeblackribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Blue, s-type)":
            python:
                gift_input = "stypeblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Dark Purple, s-type)":
            python:
                gift_input = "stypedarkpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (White, s-type)":
            python:
                gift_input = "stypedefribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Emerald, s-type)":
            python:
                gift_input = "stypeemeraldribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gray, s-type)":
            python:
                gift_input = "stypegrayribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Green, s-type)":
            python:
                gift_input = "stypegreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Light Purple, s-type)":
            python:
                gift_input = "stypelightpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Peach, s-type)":
            python:
                gift_input = "stypepeachribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pink, s-type)":
            python:
                gift_input = "stypepinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Platinum, s-type)":
            python:
                gift_input = "stypeplatinumribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Red, s-type)":
            python:
                gift_input = "styperedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Ruby, s-type)":
            python:
                gift_input = "styperubyribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Sapphire, s-type)":
            python:
                gift_input = "stypesapphireribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Silver, s-type)":
            python:
                gift_input = "stypesilverribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Teal, s-type)":
            python:
                gift_input = "stypetealribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Wine, s-type)":
            python:
                gift_input = "stypewineribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Yellow, s-type)":
            python:
                gift_input = "stypeyellowribbon.gift"
                give_custom_gift(gift_input)
        "White and Navy Blue Dress":
            python:
                gift_input = "whiteandnavybluedress.gift"
                give_custom_gift(gift_input)
        "Shirt (Pink)":
            python:
                gift_input = "pinkshirt.gift"
                give_custom_gift(gift_input)
        "Return":
            return
    return

###############################################################3

label android_menu_es:
    menu:
        "Regalos":
            jump giftmenu_es
        "Afecto":
            jump affectionmenu_es
        "Changelog":
            jump changelog_es
        "Nota de Just (porteador)":
            jump notas_es
        "Volver":
            return

label notas_es:
    "Volviendo a los clásicos, ¿eh?"
    "Nada que ignorar..."
    return

label changelog_es:
    "Uy, uy, uy..."
    "Pues nada, se agregaron las notificaciones de Android otra vez."
    "También volvió el menú de Android."
    "Y una nueva función de accesibilidad."
    "Y para que no se pierda la costumbre..."
    "Chupala  E n c o d e r s."
    return

label affectionmenu_es:
    "El afecto de [persistent._mas_monika_nickname] es [store._mas_getAffection()] puntos."
    return

label giftmenu_es:
    menu:
        "Escribe un regalo":
            call screen give_custom_gift_screen_es
        "Regalos predefinidos":
            call giftmenu_predefined_es
        "Menú de regalos dinámico (Todos los sprites posibles)":
            jump giftmenu_dynamic_es
        "Regresar":
            return
    return

label giftmenu_dynamic_es:
    python:
        from store.mas_sprites_json import giftname_map
        import os

        sorted_giftnames = sorted([
            giftname for giftname in giftname_map.keys()
            if not giftname.startswith("__")
        ])
        items = [
            (giftname + ".gift", giftname + ".gift", False, False)
            for giftname in sorted_giftnames
        ]
        display_area = store.mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA
        scroll_align = store.mas_ui.SCROLLABLE_MENU_XALIGN
        final_item = ("Regresar", False, False, False, 20)

    call screen mas_gen_scrollable_menu(items, display_area, scroll_align, final_item)
    $ result = _return

    if result and result not in ("Return", "Regresar"):
        python:
            gift_path = os.path.join(renpy.config.basedir, "characters", result)
            if not os.path.exists(gift_path):
                with open(gift_path, "w") as f:
                    f.write("")
        $ give_custom_gift(result)
    return

screen dynamic_gift_menu_es():
    tag menu
    vbox:
        spacing 10
        for gift in get_unregifted_gifts():
            textbutton gift.replace(".gift", "") action Function(give_custom_gift, gift)
        textbutton "Regresar" action Return()

label giftmenu_predefined_es:

    menu:
        "Cinta con temática del orgullo bisexual":
            python:
                gift_input = "bisexualpridethemedribbon.gift"
                give_custom_gift(gift_input)
        "Cinta blanca y negra":
            python:
                gift_input = "blackandwhiteribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color bronce":
            python:
                gift_input = "bronzeribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color marrón":
            python:
                gift_input = "brownribbon.gift"
                give_custom_gift(gift_input)
        "Cinta con degradado":
            python:
                gift_input = "gradientribbon.gift"
                give_custom_gift(gift_input)
        "Cinta con degradado de bajo poliéster":
            python:
                gift_input = "lowpolygradientribbon.gift"
                give_custom_gift(gift_input)
        "Cinta con degradado arco iris":
            python:
                gift_input = "rainbowgradientribbon.gift"
                give_custom_gift(gift_input)
        "Cinta con lunares blancos sobre rojo":
            python:
                gift_input = "whiteonredpolkadotribbon.gift"
                give_custom_gift(gift_input)
        "Cinta cielo negro estrellado":
            python:
                gift_input = "starryblackskyribbon.gift"
                give_custom_gift(gift_input)
        "Cinta de cielo rojo estrellado":
            python:
                gift_input = "starryredskyribbon.gift"
                give_custom_gift(gift_input)
        "Cinta con rayas azules y blancas":
            python:
                gift_input = "pinkandwhitestripedribbon.gift"
                give_custom_gift(gift_input)
        "Cinta con temática del orgullo transexual":
            python:
                gift_input = "transgenderpridethemedribbon.gift"
                give_custom_gift(gift_input)
        "Horquilla de luna creciente":
            python:
                gift_input = "crescentmoonhairclip.gift"
                give_custom_gift(gift_input)
        "Horquilla de fantasma":
            python:
                gift_input = "ghosthairclip.gift"
                give_custom_gift(gift_input)
        "Horquilla de calabaza":
            python:
                gift_input = "pumpkinhairclip.gift"
                give_custom_gift(gift_input)
        "Horquilla de murciélago":
            python:
                gift_input = "bathairclip.gift"
                give_custom_gift(gift_input)
        "Gargantilla (Cadena, Plata)":
            python:
                gift_input = "chokerchainsilver.gift"
                give_custom_gift(gift_input)
        "Gargantilla de margaritas blancas":
            python:
                gift_input = "chokerdaisywhite.gift"
                give_custom_gift(gift_input)
        "Gargantilla verde esmeralda":
            python:
                gift_input = "chokeremeraldgreen.gift"
                give_custom_gift(gift_input)
        "Gargantillad de plata brillante":
            python:
                gift_input = "chokerglitterbeadsilver.gift"
                give_custom_gift(gift_input)
        "Gargantilla de lazo rojo":
            python:
                gift_input = "chokerribbonred.gift"
                give_custom_gift(gift_input)
        "Gargantilla de volantes rojos":
            python:
                gift_input = "chokerrufflesred.gift"
                give_custom_gift(gift_input)
        "Gargantilla blanca de seda":
            python:
                gift_input = "chokersilkwhite.gift"
                give_custom_gift(gift_input)
        "Gargantilla con pinchos de estrellas":
            python:
                gift_input = "chokerspikedstar.gift"
                give_custom_gift(gift_input)
        "Gargantilla de espiral negra":
            python:
                gift_input = "chokerspiralblack.gift"
                give_custom_gift(gift_input)
        "Gargantilla de hilos":
            python:
                gift_input = "chokerthreadribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color negro":
            python:
                gift_input = "miniblackribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color rosa oscuro":
            python:
                gift_input = "minidarkpinkribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color gris":
            python:
                gift_input = "minigrayribbon.gift" 
                give_custom_gift(gift_input)
        "Cintilla color anaranjado":
            python:
                gift_input = "miniorangeribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color verde pálido":
            python:
                gift_input = "minipalegreenribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color rosa":
            python:
                gift_input = "minipinkribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color púrpura":
            python:
                gift_input = "minipurpleribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color rojo":
            python:
                gift_input = "miniredribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color azul royal":
            python:
                gift_input = "miniroyalblueribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color azul cielo":
            python:
                gift_input = "miniskyblueribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color blanco":
            python:
                gift_input = "miniwhiteribbon.gift"
                give_custom_gift(gift_input)
        "Cintilla color amarillo":
            python:
                gift_input = "miniyellowribbon.gift"
                give_custom_gift(gift_input)
        "Corpiño con volantes color rojo":
            python:
                gift_input = "braletteredruffles.gift"
                give_custom_gift(gift_input)
        "Camisa de flores":
            python:
                gift_input = "buttonupflowered.gift"
                give_custom_gift(gift_input)
        "Vestido color azul oscuro brillante":
            python:
                gift_input = "dressdarkbluesparkle.gift"
                give_custom_gift(gift_input)
        "Bikini de color negro con escote de corazón":
            python:
                gift_input = "heartcutbikiniblack.gift"
                give_custom_gift(gift_input)
        "Bikini de color verde con escote de corazón":
            python:
                gift_input = "heartcutbikinigreen.gift"
                give_custom_gift(gift_input)
        "Bikini de color rosa con escote de corazón":
            python:
                gift_input = "heartcutbikinipink.gift"
                give_custom_gift(gift_input)
        "Bikini de color púrpura con escote de corazón":
            python:
                gift_input = "heartcutbikinipurple.gift"
                give_custom_gift(gift_input)
        "Bikini de color blanco con escote de corazón":
            python:
                gift_input = "heartcutbikiniwhite.gift"
                give_custom_gift(gift_input)
        "Bikini de color amarillo con escote de corazón":
            python:
                gift_input = "heartcutbikiniyellow.gift"
                give_custom_gift(gift_input)
        "Uniforme de la academia Shuchi'in":
            python:
                gift_input = "shuchiinacademyuniform.gift"
                give_custom_gift(gift_input)
        "Suéter color negro sin mangas":
            python:
                gift_input = "sleevelessturtleneckblack.gift"
                give_custom_gift(gift_input)
        "Camiseta de Jurassic Park":
            python:
                gift_input = "tshirtjurassicpark.gift"
                give_custom_gift(gift_input)
        "Camiseta de Jurassic World":
            python:
                gift_input = "tshirtjurassicworld.gift"
                give_custom_gift(gift_input)
        "Camiseta blanca de tirantes cruzados de corte en V":
            python:
                gift_input = "vcutcrossedstrapstanktopwhite.gift"
                give_custom_gift(gift_input)
        "Pendientes de perlas":
            python:
                gift_input = "pearlearrings.gift"
                give_custom_gift(gift_input)
        "Piercings negro-plata":
            python:
                gift_input = "blacksilverpiercings.gift"
                give_custom_gift(gift_input)
        "Vestido de color verde":
            python:
                gift_input = "greendress.gift"
                give_custom_gift(gift_input)
        "Chaqueta color marrón":
            python:
                gift_input = "brownwinterjacket.gift"
                give_custom_gift(gift_input)
        "Camisa (pon cara de felicidad)":
            python:
                gift_input = "putonahappyfaceshirt.gift"
                give_custom_gift(gift_input)
        "Camisa de color azul":
            python:
                gift_input = "blueshirt.gift"
                give_custom_gift(gift_input)
        "Camisa (descansa aquí)":
            python:
                gift_input = "resthereshirt.gift"
                give_custom_gift(gift_input)
        "Chaleco jersey color azul":
            python:
                gift_input = "bluesweatervest.gift"
                give_custom_gift(gift_input)
        "Camiseta color blanco":
            python:
                gift_input = "tanktop.gift"
                give_custom_gift(gift_input)
        "Jersey beige de cuello alto":
            python:
                gift_input = "beigeturtlenecksweater.gift"
                give_custom_gift(gift_input)
        "Sudadera color verde con capucha":
            python:
                gift_input = "greenhoodie.gift"
                give_custom_gift(gift_input)
        "YoRHa No.2 Type B":
            python:
                gift_input = "2bcosplay.gift"
                give_custom_gift(gift_input)
        "Collar de ancla":
            python:
                gift_input = "anchor_necklace.gift"
                give_custom_gift(gift_input)
        "Collar Animal Crossing":
            python:
                gift_input = "animalcrossing_necklace.gift"
                give_custom_gift(gift_input)
        "Collar de cactus":
            python:
                gift_input = "cactus_necklace.gift"
                give_custom_gift(gift_input)
        "Collar de cadena dorada":
            python:
                gift_input = "goldchain_necklace.gift"
                give_custom_gift(gift_input)
        "Collar de concha de caracol":
            python:
                gift_input = "snailshell_necklace.gift"
                give_custom_gift(gift_input)
        "Collar estrella púrpura":
            python:
                gift_input = "star_necklace.gift"
                give_custom_gift(gift_input)
        "Collar de girasol":
            python:
                gift_input = "sunflower_necklace.gift"
                give_custom_gift(gift_input)
        "Collar Triforce":
            python:
                gift_input = "triforce_necklace.gift"
                give_custom_gift(gift_input)
        "Horquilla de cereza":
            python:
                gift_input = "cherryhairclip.gift"
                give_custom_gift(gift_input)
        "Horquilla de corazón":
            python:
                gift_input = "hearthairclip.gift"
                give_custom_gift(gift_input)
        "Horquilla 8ª nota":
            python:
                gift_input = "musicnotehairclip.gift"
                give_custom_gift(gift_input)
        "Cinta color café":
            python:
                gift_input = "coffeeribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color oro":
            python:
                gift_input = "goldribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color rosa caliente":
            python:
                gift_input = "hotpinkribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color lila":
            python:
                gift_input = "lilacribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color verde lima":
            python:
                gift_input = "limegreenribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color azul marino":
            python:
                gift_input = "navyblueribbon.gift"
                give_custom_gift(gift_input)
        "Cinta colo anaranjado":
            python:
                gift_input = "orangeribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color púpura royal":
            python:
                gift_input = "royalpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color azul cielo":
            python:
                gift_input = "skyblueribbon.gift"
                give_custom_gift(gift_input)
        "Kimono rosado":
            python:
                gift_input = "pinkkimono.gift"
                give_custom_gift(gift_input)
        "Jersey con rayas blancas y negras":
            python:
                gift_input = "blackandwhitestripedpullover.gift"
                give_custom_gift(gift_input)
        "Lazo de color negro":
            python:
                gift_input = "blackbow.gift"
                give_custom_gift(gift_input)
        "Jersey color vino asimétrico":
            python:
                gift_input = "wineasymmetricalpullover.gift"
                give_custom_gift(gift_input)
        "Flor rosada":
            python:
                gift_input = "pinkflower.gift"
                give_custom_gift(gift_input)
        "Cinta gemela color azul":
            python:
                gift_input = "bluetwinribbon.gift"
                give_custom_gift(gift_input)
        "Cinta gemela color verde":
            python:
                gift_input = "greentwinribbon.gift"
                give_custom_gift(gift_input)
        "Cinta gemela color rosa":
            python:
                gift_input = "pinktwinribbon.gift"
                give_custom_gift(gift_input)
        "Cinta gemela color amarillo":
            python:
                gift_input = "yellowtwinribbon.gift"
                give_custom_gift(gift_input)
        "Bikini de concha":
            python:
                gift_input = "shellbikini.gift"
                give_custom_gift(gift_input)
        "Hatsune Miku":
            python:
                gift_input = "hatsunemikucosplay.gift"
                give_custom_gift(gift_input)
        "Sakuya Izayoi":
            python:
                gift_input = "sakuyaizayoicosplay.gift"
                give_custom_gift(gift_input)
        "Jersey sin hombros":
            python:
                gift_input = "shoulderlesssweater.gift"
                give_custom_gift(gift_input)
        "Cinta azul 8-bit":
            python:
                gift_input = "8blueribbon.gift"
                give_custom_gift(gift_input)
        "Cinta esmeralda 8-bit":
            python:
                gift_input = "8emeraldribbon.gift"
                give_custom_gift(gift_input)
        "Cinta blanca 8-bit":
            python:
                gift_input = "8whiteribbon.gift"
                give_custom_gift(gift_input)
        "Cinta amdek ámbar":
            python:
                gift_input = "amdekamberribbon.gift"
                give_custom_gift(gift_input)
        "Cinta game boy verde":
            python:
                gift_input = "gameboygreenribbon.gift"
                give_custom_gift(gift_input)
        "Cinta púrpura 8-bit":
            python:
                gift_input = "8purpleribbon.gift"
                give_custom_gift(gift_input)
        "Cinta roja 8-bit":
            python:
                gift_input = "8redribbon.gift"
                give_custom_gift(gift_input)
        "Cinta super game boy verde":
            python:
                gift_input = "supergameboygreenribbon.gift"
                give_custom_gift(gift_input)
        "Gargantilla corazón":
            python:
                gift_input = "heartchoker.gift"
                give_custom_gift(gift_input)
        "Gargantilla floreada":
            python:
                gift_input = "floweredchoker.gift"
                give_custom_gift(gift_input)
        "Gargantilla simple":
            python:
                gift_input = "simplechoker.gift"
                give_custom_gift(gift_input)
        "Coletero azul de conejita":
            python:
                gift_input = "bluebunnyscrunchie.gift"
                give_custom_gift(gift_input)
        "Cinta color negro tipo-s":
            python:
                gift_input = "stypeblackribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color azul tipo-s":
            python:
                gift_input = "stypeblueribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color púpura oscuro tipo-s":
            python:
                gift_input = "stypedarkpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color blanco tipo-s":
            python:
                gift_input = "stypedefribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color esmeralda tipo-s":
            python:
                gift_input = "stypeemeraldribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color gris tipo-s":
            python:
                gift_input = "stypegrayribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color verde tipo-s":
            python:
                gift_input = "stypegreenribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color púpura claro tipo-s":
            python:
                gift_input = "stypelightpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color melocotón tipo-s":
            python:
                gift_input = "stypepeachribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color rosa tipo-s":
            python:
                gift_input = "stypepinkribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color platino tipo-s":
            python:
                gift_input = "stypeplatinumribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color rojo tipo-s":
            python:
                gift_input = "styperedribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color ruby tipo-s":
            python:
                gift_input = "styperubyribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color safiro tipo-s":
            python:
                gift_input = "stypesapphireribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color plata tipo-s":
            python:
                gift_input = "stypesilverribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color turqueza tipo-s":
            python:
                gift_input = "stypetealribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color vino tipo-s":
            python:
                gift_input = "stypewineribbon.gift"
                give_custom_gift(gift_input)
        "Cinta color amarillo tipo-s":
            python:
                gift_input = "stypeyellowribbon.gift"
                give_custom_gift(gift_input)
        "Vestido blanco con azul marino":
            python:
                gift_input = "whiteandnavybluedress.gift"
                give_custom_gift(gift_input)
        "Camisa color rosa":
            python:
                gift_input = "pinkshirt.gift"
                give_custom_gift(gift_input)
        "Regresar":
            return

screen give_custom_gift_screen_en():
    tag menu

    add Solid("#000000c0") at gift_bg_fadein

    frame at gift_frame_appear:
        xalign 0.5
        yalign 0.25
        xsize 960
        ysize 320
        background Frame("gui/frame.png", 960, 64)
        padding (0, 0, 0, 0)

        has vbox
        spacing 24
        xalign 0.5
        yalign 0.5

        hbox:
            spacing 32
            xalign 0.5
            text "Enter the name of the gift for Monika\n(include the '.gift' or '.txt' extension):" xalign 0.5 size 24 color "#FFD9E8" outlines [(2, "#000", 0, 0)] at gift_text_appear
            textbutton "Give Gift":
                at gift_button_appear
                action [Function(give_custom_gift, gift_input), Return()]
                style "gift_button_modern"
            textbutton "Close":
                at gift_button_appear
                action Return()
                style "gift_button_modern"

        input value VariableInputValue("gift_input") length 999 xalign 0.5 xsize 420 color "#333" outlines [(1, "#FFD9E8", 0, 0)] at gift_input_appear

screen give_custom_gift_screen_es():
    tag menu

    add Solid("#000000c0") at gift_bg_fadein

    frame at gift_frame_appear:
        xalign 0.5
        yalign 0.25
        xsize 960
        ysize 320
        background Frame("gui/frame.png", 960, 64)
        padding (0, 0, 0, 0)

        has vbox
        spacing 24
        xalign 0.5
        yalign 0.5

        hbox:
            spacing 32
            xalign 0.5
            text "Escribe el nombre del regalo para Monika\n(coloca la extensión '.gift' o '.txt' según\n corresponda):" xalign 0.5 size 24 color "#FFD9E8" outlines [(2, "#000", 0, 0)] at gift_text_appear
            textbutton "Dar Regalo":
                at gift_button_appear
                action [Function(give_custom_gift, gift_input), Return()]
                style "gift_button_modern"
            textbutton "Cerrar":
                at gift_button_appear
                action Return()
                style "gift_button_modern"

        input value VariableInputValue("gift_input") length 999 xalign 0.5 xsize 420 color "#333" outlines [(1, "#FFD9E8", 0, 0)] at gift_input_appear


transform gift_bg_fadein:
    alpha 0.0
    linear 0.3 alpha 1.0

transform gift_frame_appear:
    alpha 0.0
    zoom 0.9
    linear 0.25 alpha 1.0 zoom 1.0

transform gift_text_appear:
    alpha 0.0
    yoffset 20
    linear 0.3 alpha 1.0 yoffset 0

transform gift_input_appear:
    alpha 0.0
    xoffset -30
    linear 0.3 alpha 1.0 xoffset 0

transform gift_button_appear:
    alpha 0.0
    yoffset 20
    linear 0.2 alpha 1.0 yoffset 0

style gift_button_modern is button:
    xsize 180
    ysize 48
    font "gui/font/RifficFree-Bold.ttf"
    size 20
    color "#fff"
    hover_color "#FFD9E8"
    outlines [(2, "#b59", 0, 0)]