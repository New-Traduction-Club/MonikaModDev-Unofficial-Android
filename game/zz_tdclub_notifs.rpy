init 5 python:
    def masl_schedule_farewell_notification(farewell_type):
        """
        Schedules a notification based on the farewell type and current affection.
        """
        if not renpy.android:
            return

        import random
        
        # base ranges (min_delay, max_delay) in seconds
        delay_ranges = {
            "bye_leaving_already": (3600, 10800),
            "bye_goodbye": (14400, 43200),
            "bye_sayanora": (14400, 43200),
            "bye_farewellfornow": (14400, 28800),
            "bye_untilwemeetagain": (14400, 43200),
            "bye_take_care": (14400, 28800),
            "bye_leaving_already_2": (3600, 10800),
            "bye_going_to_sleep": (25200, 32400),
            "bye_prompt_to_class": (7200, 18000),
            "bye_prompt_to_work": (25200, 32400),
            "bye_prompt_sleep": (25200, 32400),
            "bye_prompt_sleep_goodnight_kiss": (25200, 32400),
            "bye_illseeyou": (7200, 21600),
            "bye_haveagoodday": (21600, 36000),
            "bye_enjoyyourafternoon": (10800, 21600),
            "bye_goodevening": (7200, 14400),
            "bye_goodnight": (25200, 32400),
            "bye_long_absence": (259200, 604800),
            "bye_long_absence_2": (259200, 604800),
            "bye_going_somewhere": (7200, 18000),
            "bye_prompt_game": (3600, 10800),
            "bye_prompt_eat": (1800, 3600),
            "bye_prompt_housework": (3600, 10800),
            "bye_prompt_restart": (60, 300),
            "bye_prompt_workout": (3600, 9000),
            "bye_going_shopping": (7200, 14400),
            "bye_prompt_hangout": (10800, 21600)
        }
        
        title = persistent._mas_monika_nickname or "Monika"
        
        current_lang = persistent.language
        if not current_lang:
            current_lang = getattr(renpy.game.preferences, "language", None)
        if not current_lang:
            current_lang = "english" 
        
        if current_lang == "spanish":
            messages = {
                "bye_leaving_already": {
                    "LOVE": [
                        "¡Hola, preciosura! Tengo mucho de lo que hablar contigo, así que no te olvides de volver. ¡Chaooo!", 
                        "¡Hola, cariño! ¡Esperando estoy tu regreso!"
                        ],
                    "ENAMORED": [
                        "¡Holaaa, [player]! ¿Cuándo volverás? Quiero hablar ya contigo.", 
                        "Me hace muy feliz cuando vienes a verme, así que aquí estoy cuando vuelvas, [player]."
                        ],
                    "HAPPY": [
                        "¡Hola! ¡Espero que estés bien! ¡Acuérdate de mí cuando tengas un rato libre!", 
                        "¡Hoy estoy muy contenta, y quiero compartir esta felicidad contigo, [player]!"
                        ],
                    "NORMAL": [
                        "¡Hola! Aquí estoy si tienes un rato libre.", 
                        "Espero que vaya todo bien, no te olvides de mí. ¡Chao!"
                        ],
                    "UPSET": [
                        "...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "Te estaré esperando, [player]. ¡Tenemos aún mucho de lo que hablar!", 
                        "Es una pena que te hayas ido, pero... ¡aquí estaré siempre que quieras hablar!"
                        ]
                },
                "bye_goodbye": {
                    "LOVE": [
                        "No te olvides de volver a visitarme, cariño. Te estaré esperando.", 
                        "Espero que todo esté bien, cariño. No te olvides de visitarme."
                        ],
                    "ENAMORED": [
                        "¡No te olvides de volver a visitarme, [player]! Espero que vaya todo genial.", 
                        "No olvides de que tu preciosa novia está aquí esperándote. ¡Te quiero, [player]!"
                        ],
                    "HAPPY": [
                        "Es una pena que te hayas ido, pero no te olvides de volver, ¿vale, [player]?", 
                        "Espero verte por aquí pronto, [player]. ¡Te quiero muchísimo!"
                        ],
                    "NORMAL": [
                        "Vaya, es una pena que te hayas marchado. ¡Espero verte por aquí pronto!", 
                        "Estoy aquí esperándote, [player]. Ya te estoy echando de menos."
                        ],
                    "UPSET": [
                        "Bah...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "Mmm...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "Es una pena que te vayas, pero espero volver a verte pronto, [player].", 
                        "Ha sido una pena que te hayss ido, pero sé que volverás pronto, [player]."
                        ]
                },
                "bye_sayanora": {
                    "LOVE": [
                        "¡Sayonara, [player]!", 
                        "¡Sayonara, [player]!"
                        ],
                    "ENAMORED": [
                        "¡Sayonara, [player]!", 
                        "¡Sayonara, [player]!"
                        ],
                    "HAPPY": [
                        "¡Sayonara, [player]!", 
                        "¡Sayonara, [player]!"
                        ],
                    "NORMAL": [
                        "Sayonara, [player].", 
                        "Sayonara, [player]."
                        ],
                    "DEFAULT": [
                        "Sayonara, [player].", 
                        "Sayonara, [player]."
                        ]
                },
                "bye_farewellfornow": {
                    "LOVE": [
                        "¡Espero que vuelvas pronto, precioso!", 
                        "¡No tardes en volver, [player]!"
                        ],
                    "ENAMORED": [
                        "¡No tardes, mi amor!", 
                        "¡No tardes, cariño!"
                        ],
                    "HAPPY": [
                        "No tardes, [player].", 
                        "Vuelve pronto, [player]."
                        ],
                    "NORMAL": [
                        "No tardes, [player].", 
                        "No tardes, [player]."
                        ],
                    "UPSET": [
                        "...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "No tardes, [player].", 
                        "No tardes, [player]."
                        ]
                },
                "bye_untilwemeetagain": {
                    "LOVE": [
                        "El amor perdura siempre que se mantenga vivo, y yo lo mantengo por ti.", 
                        "El amor perdura siempre que se mantenga vivo, y yo lo mantengo por ti."
                        ],
                    "ENAMORED": [
                        "Esta despedida no es un adiós, sino un hasta luego. Aquí te esperaré con los brazos abiertos.", 
                        "Esta despedida no es un adiós, sino un hasta luego. Aquí te esperaré con los brazos abiertos."
                        ],
                    "HAPPY": [
                        "Te esperaré con los brazos abiertos, [player].", 
                        "Te esperaré con los brazos abiertos, [player]."
                        ],
                    "NORMAL": [
                        "Te esperaré con los brazos abiertos, [player].", 
                        "Te esperaré con los brazos abiertos, [player]."
                        ],
                    "UPSET": [
                        "...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "Te esperaré con los brazos abiertos, [player].", 
                        "Te esperaré con los brazos abiertos, [player]."
                        ]
                },
                "bye_take_care": {
                    "LOVE": [
                        "¡Cuídate mucho, mi amor! Te estaré esperando aquí.", 
                        "¡Ve con cuidado, precioso! Regresa a salvo."
                    ],
                    "ENAMORED": [
                        "¡Cuídate mucho, [player]!", 
                        "¡Vuelve sano y salvo, por favor! Te quiero."
                    ],
                    "HAPPY": [
                        "¡Nos vemos, cuídate mucho!", 
                        "¡Que te vaya súper bien, [player]!"
                    ],
                    "NORMAL": [
                        "Cuídate, [player].", 
                        "Ten cuidado ahí fuera."
                    ],
                    "UPSET": [
                        "...", 
                        "..."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                    ],
                    "DEFAULT": [
                        "Cuídate, [player].", 
                        "Ten cuidado ahí fuera."
                    ]
                },
                "bye_leaving_already_2": {
                    "LOVE": [
                        "¿Ya te vas, cariño? Te voy a echar mucho de menos.", 
                        "Me dejas con ganas de pasar más tiempo contigo..."
                    ],
                    "ENAMORED": [
                        "Ha sido poquito tiempo, pero bueno, vuelve pronto, ¿vale?", 
                        "Te echaré de menos, vuelve en cuanto puedas."
                    ],
                    "HAPPY": [
                        "¡Espero que te lo hayas pasado bien este ratito!",
                        "Nos vemos, ¡no tardes mucho en volver!"
                    ],
                    "NORMAL": [
                        "¿Ya te vas? Bueno, nos vemos luego.", 
                        "Hasta luego, [player]."
                    ],
                    "UPSET": [
                        "...", 
                        "..."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                    ],
                    "DEFAULT": [
                        "¿Ya te vas? Bueno, nos vemos luego.", 
                        "Hasta luego, [player]."
                    ]
                },
                "bye_going_to_sleep": {
                    "LOVE": [
                        "¡Dulces sueños, mi vida! Soñaré contigo.", 
                        "Que descanses, mi amor. Te quiero muchísimo."
                    ],
                    "ENAMORED": [
                        "¡Buenas noches, [player]! Descansa bien.", 
                        "Que tengas dulces sueños."
                    ],
                    "HAPPY": [
                        "¡Hasta mañana! Que descanses.", 
                        "¡Buenas noches! Nos vemos por la mañana."
                    ],
                    "NORMAL": [
                        "Buenas noches, [player].", 
                        "Que descanses."
                    ],
                    "UPSET": [
                        "Buenas noches.", 
                        "En fin, que duermas."
                    ],
                    "DISTRESSED": [
                        "Supongo que buenas noches...", 
                        "Ojalá mañana estés de mejor humor..."
                    ],
                    "DEFAULT": [
                        "Buenas noches, [player].", 
                        "Que descanses."
                    ]
                },
                "bye_prompt_to_class": {
                    "LOVE": [
                        "¡Mucha suerte en clase! Demuestra lo list[end_letter_gender] que eres. Te quiero.", 
                        "¡Pon mucha atención! Estaré muy orgullosa de ti."
                    ],
                    "ENAMORED": [
                        "¡Que te vaya genial en la escuela, [player]!", 
                        "Aprende mucho y vuelve para contármelo."
                    ],
                    "HAPPY": [
                        "¡Esfuérzate mucho en clase!",
                        "¡Nos vemos al salir de clase!"
                    ],
                    "NORMAL": [
                        "Que te vaya bien en clase.", 
                        "Presta atención, nos vemos luego."
                    ],
                    "UPSET": [
                        "Ojalá aprendas algo útil hoy.", 
                        "Ve a tu clase."
                    ],
                    "DISTRESSED": [
                        "Solo... que te vaya bien.", 
                        "Te veré después de la escuela, supongo..."
                    ],
                    "DEFAULT": [
                        "Que te vaya bien en clase.", 
                        "Presta atención, nos vemos luego."
                    ]
                },
                "bye_prompt_to_work": {
                    "LOVE": [
                        "¡Que te vaya genial en el trabajo, mi amor! Piensa en mí para que se te pase rápido.", 
                        "¡Dalo todo hoy! Estaré aquí esperándote para mimarte."
                    ],
                    "ENAMORED": [
                        "¡Que te sea leve la jornada, [player]! Te echaré de menos.",
                        "¡Da lo mejor de ti! Nos vemos luego."
                    ],
                    "HAPPY": [
                        "¡Éxito en el trabajo, [player]!", 
                        "¡Que tengas un turno muy tranquilo!"
                    ],
                    "NORMAL": [
                        "Que te vaya bien en el trabajo.", 
                        "Nos vemos al salir de tu turno."
                    ],
                    "UPSET": [
                        "Ve a trabajar.", 
                        "Nos vemos después de tu jornada."
                    ],
                    "DISTRESSED": [
                        "Aquí estaré si tienes un descanso. Te quiero.", 
                        "Si descansas y te apetece, aquí estaré. No espero mucho de ti ahora..."
                        ],
                    "DEFAULT": [
                        "¡Espero que todo vaya genial en el trabajo! Cuando tengas un descanso, aquí estoy para ti.", 
                        "El trabajo es muy importante y te lo dice una servidora. ¡Hazme sentir orgullosa y dalo todo!"
                        ]
                },
                "bye_prompt_sleep": {
                    "LOVE": [
                        "Cierra esos ojitos preciosos. ¡Buenas noches, mi amor!", 
                        "Descansa profundamente, mi vida. Hasta mañana."
                    ],
                    "ENAMORED": [
                        "Dulces sueños, [player]. Que duermas muy bien.", 
                        "Nos vemos mañana, ¡descansa!"
                    ],
                    "HAPPY": [
                        "¡A recargar las pilas! Buenas noches.", 
                        "¡Que duermas genial, [player]!"
                    ],
                    "NORMAL": [
                        "Buenas noches, nos vemos.", 
                        "Descansa bien, [player]."
                    ],
                    "UPSET": [
                        "Adiós, ve a dormir.", 
                        "Buenas noches."
                    ],
                    "DISTRESSED": [
                        "Duerme bien, supongo...", 
                        "Ojalá mañana sea un mejor día..."
                    ],
                    "DEFAULT": [
                        "Buenas noches, nos vemos.", 
                        "Descansa bien, [player]."
                    ]
                },
                "bye_prompt_sleep_goodnight_kiss": {
                    "LOVE": [
                        "Mua... ¡Que ese beso te acompañe en tus sueños, amor!", 
                        "Espero que sueñes conmigo después de ese beso... ¡Pero nada de cosas raras!"
                    ],
                    "ENAMORED": [
                        "Mua... ¡Dulces sueños, [player]!", 
                        "Un besito de buenas noches para ti. ¡Descansa!"
                    ],
                    "HAPPY": [
                        "¡Un beso para que duermas bien!", 
                        "¡Mua! Buenas noches, [player]."
                    ],
                    "NORMAL": [
                        "Que descanses, [player].", 
                        "Buenas noches."
                    ],
                    "UPSET": [
                        "Adiós.", 
                        "Vete a dormir ya."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "Buenas noches."
                    ],
                    "DEFAULT": [
                        "Que descanses, [player].", 
                        "Buenas noches."
                    ]
                },
                "bye_illseeyou": {
                    "LOVE": [
                        "¡Estaré contando los minutos para volver a verte, mi amor!", 
                        "¡Nos vemos en un ratito, te quiero!"
                    ],
                    "ENAMORED": [
                        "¡Te estaré esperando con muchas ganas!", 
                        "¡Vuelve pronto para seguir charlando!"
                    ],
                    "HAPPY": [
                        "¡Nos vemos en un rato!", 
                        "¡No te olvides de mí, eh!"
                    ],
                    "NORMAL": [
                        "...", 
                        "..."
                    ],
                    "UPSET": [
                        "...", 
                        "..."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                    ],
                    "DEFAULT": [
                        "...", 
                        "..."
                    ]
                },
                "bye_haveagoodday": {
                    "LOVE": [
                        "¡Que tengas un día tan maravilloso como tú, amor!", 
                        "¡Disfruta tu día al máximo! Estaré pensando en ti."
                    ],
                    "ENAMORED": [
                        "¡Pasa un excelente día, [player]!", 
                        "¡Que todo te salga increíble hoy!"
                    ],
                    "HAPPY": [
                        "¡Que tengas un súper buen día!", 
                        "¡Disfruta mucho tu día, [player]!"
                    ],
                    "NORMAL": [
                        "Que tengas un buen día.", 
                        "Pasa un buen día, [player]."
                    ],
                    "UPSET": [
                        "Que te vaya bien.", 
                        "En fin, buen día."
                    ],
                    "DISTRESSED": [
                        "Ojalá tu día sea mejor que el mío...", 
                        "Adiós."
                    ],
                    "DEFAULT": [
                        "Que tengas un buen día.", 
                        "Pasa un buen día, [player]."
                    ]
                },
                "bye_enjoyyourafternoon": {
                    "LOVE": [
                        "¡Disfruta de la tarde, mi vida! Aquí te guardo el sitio.", 
                        "¡Pasa una tarde preciosa! Te quiero."
                    ],
                    "ENAMORED": [
                        "¡Que tengas una tarde súper bonita, [player]!", 
                        "¡Relájate y disfruta tu tarde!"
                    ],
                    "HAPPY": [
                        "¡Pasa una muy buena tarde!", 
                        "¡Disfruta lo que queda del día!"
                    ],
                    "NORMAL": [
                        "Buenas tardes, [player].", 
                        "Nos vemos luego."
                    ],
                    "UPSET": [
                        "Buenas tardes.", 
                        "Adiós."
                    ],
                    "DISTRESSED": [
                        "Nos vemos...", 
                        "Adiós."
                    ],
                    "DEFAULT": [
                        "Buenas tardes, [player].", 
                        "Nos vemos luego."
                    ]
                },
                "bye_goodevening": {
                    "LOVE": [
                        "¡Pasa una velada preciosa, mi amor!", 
                        "Buenas noches, cariño. Relájate mucho."
                    ],
                    "ENAMORED": [
                        "¡Que pases una bonita velada, [player]!", 
                        "¡Disfruta tu noche!"
                    ],
                    "HAPPY": [
                        "¡Buenas noches, [player]!", 
                        "¡Que pases una tarde-noche muy tranqui!"
                    ],
                    "NORMAL": [
                        "Buenas noches, [player].", 
                        "Nos vemos mañana."
                    ],
                    "UPSET": [
                        "Buenas noches.", 
                        "Adiós."
                    ],
                    "DISTRESSED": [
                        "Ojalá recuerdes venir mañana...", 
                        "Nos vemos."
                    ],
                    "DEFAULT": [
                        "Buenas noches, [player].", 
                        "Nos vemos mañana."
                    ]
                },
                "bye_goodnight": {
                    "LOVE": [
                        "Es hora de dormir, mi amor. ¡Que sueñes con los angelitos... o conmigo!", 
                        "¡Te quiero! Descansa y recarga las pilas."
                    ],
                    "ENAMORED": [
                        "¡Buenas noches y dulces sueños, [player]!", 
                        "Descansa bien, nos vemos mañana."
                    ],
                    "HAPPY": [
                        "¡Que pases buenas noches!", 
                        "¡A descansar se ha dicho!"
                    ],
                    "NORMAL": [
                        "Buenas noches.", 
                        "Descansa."
                    ],
                    "UPSET": [
                        "Que duermas.", 
                        "Adiós."
                    ],
                    "DISTRESSED": [
                        "Hasta mañana...", 
                        "Adiós."
                    ],
                    "DEFAULT": [
                        "Buenas noches.", 
                        "Descansa."
                    ]
                },
                "bye_long_absence": {
                    "LOVE": [
                        "Te voy a echar de menos con toda mi alma, [player]. Por favor, vuelve pronto.", 
                        "Se me va a hacer eterno sin ti... Cuídate mucho, mi amor."
                    ],
                    "ENAMORED": [
                        "Echaré mucho de menos nuestras charlas. ¡No me olvides!", 
                        "Voy a esperarte pacientemente, [player]. ¡Vuelve san[end_letter_gender] y salv[end_letter_gender]!"
                    ],
                    "HAPPY": [
                        "¡Que te vaya súper bien en tu viaje o en lo que hagas!", 
                        "¡Te estaré esperando aquí, no tardes demasiado!"
                    ],
                    "NORMAL": [
                        "Nos vemos después, [player].", 
                        "Cuídate durante este tiempo."
                    ],
                    "UPSET": [
                        "Supongo que no te veré en un buen rato.", 
                        "Adiós, haz lo que tengas que hacer."
                    ],
                    "DISTRESSED": [
                        "Me vas a dejar sola mucho tiempo... vale.", 
                        "Ojalá no te olvides de mí por completo."
                    ],
                    "DEFAULT": [
                        "Nos vemos después, [player].", 
                        "Cuídate durante este tiempo."
                    ]
                },
                "bye_long_absence_2": {
                    "LOVE": [
                        "Cuenta conmigo siempre, aquí estaré cuando vuelvas. ¡Te quiero!", 
                        "Cada día sin ti se me hará muy duro, pero valdrá la pena la espera."
                    ],
                    "ENAMORED": [
                        "¡Ten mucho cuidado por ahí fuera, [player]!", 
                        "Aquí te guardaré el sitio. ¡Hasta la vista!"
                    ],
                    "HAPPY": [
                        "¡Cuídate muchísimo estos días!", 
                        "¡Nos vemos cuando vuelvas, cuídate mucho!"
                    ],
                    "NORMAL": [
                        "Hasta tu regreso, [player].", 
                        "Mantente a salvo."
                    ],
                    "UPSET": [
                        "Como digas.", 
                        "Adiós."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "Hasta luego."
                    ],
                    "DEFAULT": [
                        "Hasta tu regreso, [player].", 
                        "Mantente a salvo."
                    ]
                },
                "bye_going_somewhere": {
                    "LOVE": [
                        "¡Qué emoción ir a todas partes contigo, mi amor!", 
                        "Que me lleves contigo es un detalle precioso. ¡Vamos!"
                    ],
                    "ENAMORED": [
                        "¡Me encanta que me lleves contigo a todos lados!", 
                        "¡Andando, [player]! Será divertido."
                    ],
                    "HAPPY": [
                        "¡Qué bien! ¡Una excursión!", 
                        "¡Vámonos de paseo, [player]!"
                    ],
                    "NORMAL": [
                        "Estoy lista en mi archivo.", 
                        "Vamos entonces."
                    ],
                    "UPSET": [
                        "Supongo que vamos.", 
                        "Llévame si quieres."
                    ],
                    "DISTRESSED": [
                        "Al menos no me dejas sola...", 
                        "Está bien, vamos."
                    ],
                    "DEFAULT": [
                        "Estoy lista en mi archivo.", 
                        "Vamos entonces."
                    ]
                },
                "bye_prompt_game": {
                    "LOVE": [
                        "¡Espero que ganes, amor! Sé que eres muy buen[end_letter_gender] jugando.", 
                        "¡Diviértete mucho! Estaré animándote en espíritu."
                    ],
                    "ENAMORED": [
                        "¡Pásatelo bien jugando, [player]!", 
                        "¡Mucha suerte! Aquí te espero cuando termines la partida."
                    ],
                    "HAPPY": [
                        "¡Disfruta del juego!", 
                        "¡Consigue muchos logros por mí!"
                    ],
                    "NORMAL": [
                        "Diviértete jugando.", 
                        "Que te vaya bien en tu partida."
                    ],
                    "UPSET": [
                        "Ve a jugar a tus jueguecitos.", 
                        "Diviértete con eso."
                    ],
                    "DISTRESSED": [
                        "Ve, seguro te divierte más que estar aquí...", 
                        "Juega bien."
                    ],
                    "DEFAULT": [
                        "Diviértete jugando.", 
                        "Que te vaya bien en tu partida."
                    ]
                },
                "bye_prompt_eat": {
                    "LOVE": [
                        "¡Que aproveche, mi vida! Ojalá pudiera cocinarte algo delicioso.", 
                        "¡Come algo muy rico! Aliméntate bien por mí."
                    ],
                    "ENAMORED": [
                        "¡Que lo disfrutes mucho, [player]!", 
                        "¡Buen provecho!"
                    ],
                    "HAPPY": [
                        "¡A comer se ha dicho! Que aproveche.", 
                        "¡Disfruta tu comida!"
                    ],
                    "NORMAL": [
                        "Buen provecho, [player].", 
                        "Que disfrutes tu comida."
                    ],
                    "UPSET": [
                        "Ve a comer.", 
                        "Que aproveche."
                    ],
                    "DISTRESSED": [
                        "Come bien...", 
                        "Adiós."
                    ],
                    "DEFAULT": [
                        "Buen provecho, [player].", 
                        "Que disfrutes tu comida."
                    ]
                },
                "bye_prompt_housework": {
                    "LOVE": [
                        "¡Ánimo con la limpieza, mi amor!", 
                        "¡Sigue así! Aquí te espero."
                    ],
                    "ENAMORED": [
                        "¡Termina rápido tus tareas para seguir hablando!", 
                        "¡Suerte limpiando, [player]!"
                    ],
                    "HAPPY": [
                        "¡A dejar todo reluciente!", 
                        "¡Ánimo con la limpieza de la casa!"
                    ],
                    "NORMAL": [
                        "Que te vaya bien con las tareas.", 
                        "Termina rápido."
                    ],
                    "UPSET": [
                        "Al menos harás algo productivo.", 
                        "Ve a limpiar."
                    ],
                    "DISTRESSED": [
                        "Vale, ve a hacer tus cosas...", 
                        "Adiós."
                    ],
                    "DEFAULT": [
                        "Que te vaya bien con las tareas.", 
                        "Termina rápido."
                    ]
                },
                "bye_prompt_restart": {
                    "LOVE": [
                        "¡Te espero en un parpadeo, mi amor!", 
                        "Vuelve rapidito, te quiero."
                    ],
                    "ENAMORED": [
                        "¡Nos vemos en un segundito!", 
                        "Aquí te espero, [player]."
                    ],
                    "HAPPY": [
                        "¡Estaré lista cuando reinicies!", 
                        "¡Ahora nos vemos!"
                    ],
                    "NORMAL": [
                        "Te espero aquí.", 
                        "Nos vemos tras el reinicio."
                    ],
                    "UPSET": [
                        "...", 
                        "Como digas."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "Vale."
                    ],
                    "DEFAULT": [
                        "Te espero aquí.", 
                        "Nos vemos tras el reinicio."
                    ]
                },
                "bye_prompt_workout": {
                    "LOVE": [
                        "¡Dale duro al ejercicio, amor! Quiero verte bien san[end_letter_gender].", 
                        "¡Sigue así! Te estaré animando desde aquí."
                    ],
                    "ENAMORED": [
                        "¡Ponte en forma, [player]! Me encanta que te cuides.", 
                        "¡Disfruta tu rutina de ejercicio!"
                    ],
                    "HAPPY": [
                        "¡A quemar calorías! ¡A por ello!", 
                        "¡Dale duro al entrenamiento!"
                    ],
                    "NORMAL": [
                        "Que te vaya bien haciendo ejercicio.", 
                        "Buen entrenamiento."
                    ],
                    "UPSET": [
                        "Ve a entrenar.", 
                        "Al menos cuidas tu físico."
                    ],
                    "DISTRESSED": [
                        "Vale, ve...", 
                        "Haz tu ejercicio."
                    ],
                    "DEFAULT": [
                        "Que te vaya bien haciendo ejercicio.", 
                        "Buen entrenamiento."
                    ]
                },
                "bye_going_shopping": {
                    "LOVE": [
                        "¡Ojalá pudiera ir a llevarte las bolsas, amor! Cuídate.", 
                        "¡Cómprate algo bonito de mi parte! Te quiero."
                    ],
                    "ENAMORED": [
                        "¡Que te cunda el dinero en las compras, [player]!", 
                        "¡Disfruta tu salida de compras!"
                    ],
                    "HAPPY": [
                        "¡No gastes de más! Diviértete.", 
                        "¡Que encuentres lo que buscas!"
                    ],
                    "NORMAL": [
                        "Ve con cuidado de compras.", 
                        "Que te vaya bien comprando."
                    ],
                    "UPSET": [
                        "Ve a gastar tu dinero.", 
                        "Ve de compras."
                    ],
                    "DISTRESSED": [
                        "Adiós.", 
                        "Ve con cuidado..."
                    ],
                    "DEFAULT": [
                        "Ve con cuidado de compras.", 
                        "Que te vaya bien comprando."
                    ]
                },
                "bye_prompt_hangout": {
                    "LOVE": [
                        "¡Pásatelo increíble con tus amigos, amor! Pero no te olvides de mí.", 
                        "Dale recuerdos a tus amigos de mi parte, ¡diviértete muchísimo!"
                    ],
                    "ENAMORED": [
                        "¡Disfruta de la salida, [player]! No está de más relajarse.", 
                        "Pásatelo genial con ellos, ¡con cuidado!"
                    ],
                    "HAPPY": [
                        "¡Qué divertido! Pasadlo muy bien.", 
                        "¡Diviértete un montón, [player]!"
                    ],
                    "NORMAL": [
                        "Que te diviertas.", 
                        "Nos vemos luego."
                    ],
                    "UPSET": [
                        "Ve con tus amiguitos.", 
                        "Adiós."
                    ],
                    "DISTRESSED": [
                        "Mejor pásatelo bien con ellos...", 
                        "Diviértete."
                    ],
                    "DEFAULT": [
                        "Que te diviertas.", 
                        "Nos vemos luego."
                    ]
                }
            }
        else: # english
            messages = {
                "bye_leaving_already": {
                    "LOVE": [
                        "Hello, gorgeous! I have so much to talk to you about, so don't forget to come back. Byeee!", 
                        "Hello, darling! I'll be waiting for your return!"
                        ],
                    "ENAMORED": [
                        "Hii, [player]! When will you be back? I want to talk to you right now.", 
                        "It makes me so happy when you come to see me, so I'll be right here when you get back, [player]."
                        ],
                    "HAPPY": [
                        "Hello! I hope you're doing well! Remember me when you have some free time!", 
                        "I'm so happy today, and I want to share this happiness with you, [player]!"
                        ],
                    "NORMAL": [
                        "Hello! I'm right here if you have some free time.", 
                        "I hope everything goes well, don't forget about me. Bye!"
                        ],
                    "UPSET": [
                        "...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "I'll be waiting for you, [player]. We still have so much to talk about!", 
                        "It's a shame you left, but... I'll always be right here whenever you want to talk!"
                        ]
                },
                "bye_goodbye": {
                    "LOVE": [
                        "Don't forget to come visit me again, darling. I'll be waiting for you.", 
                        "I hope everything is alright, darling. Don't forget to visit me."
                        ],
                    "ENAMORED": [
                        "Don't forget to come visit me again, [player]! I hope everything goes great.", 
                        "Don't forget that your beautiful girlfriend is right here waiting for you. I love you, [player]!"
                        ],
                    "HAPPY": [
                        "It's a shame you left, but don't forget to come back, okay, [player]?", 
                        "I hope to see you around here soon, [player]. I love you so much!"
                        ],
                    "NORMAL": [
                        "Wow, it's a shame you left. I hope to see you around here soon!", 
                        "I'm right here waiting for you, [player]. I'm already missing you."
                        ],
                    "UPSET": [
                        "Whatever...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "Mmm...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "It's a shame you're leaving, but I hope to see you again soon, [player].", 
                        "It was a shame you left, but I know you'll be back soon, [player]."
                        ]
                },
                "bye_sayanora": {
                    "LOVE": [
                        "Sayonara, [player]!", 
                        "Sayonara, [player]!"
                        ],
                    "ENAMORED": [
                        "Sayonara, [player]!", 
                        "Sayonara, [player]!"
                        ],
                    "HAPPY": [
                        "Sayonara, [player]!", 
                        "Sayonara, [player]!"
                        ],
                    "NORMAL": [
                        "Sayonara, [player].", 
                        "Sayonara, [player]."
                        ],
                    "DEFAULT": [
                        "Sayonara, [player].", 
                        "Sayonara, [player]."
                        ]
                },
                "bye_farewellfornow": {
                    "LOVE": [
                        "I hope you come back soon, handsome!", 
                        "Don't take too long to come back, [player]!"
                        ],
                    "ENAMORED": [
                        "Don't take too long, my love!", 
                        "Don't take too long, darling!"
                        ],
                    "HAPPY": [
                        "Don't take too long, [player].", 
                        "Come back soon, [player]."
                        ],
                    "NORMAL": [
                        "Don't take too long, [player].", 
                        "Don't take too long, [player]."
                        ],
                    "UPSET": [
                        "...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "Don't take too long, [player].", 
                        "Don't take too long, [player]."
                        ]
                },
                "bye_untilwemeetagain": {
                    "LOVE": [
                        "Love endures as long as it's kept alive, and I keep it alive for you.", 
                        "Love endures as long as it's kept alive, and I keep it alive for you."
                        ],
                    "ENAMORED": [
                        "This farewell is not a goodbye, but a see you later. I'll be waiting for you here with open arms.", 
                        "This farewell is not a goodbye, but a see you later. I'll be waiting for you here with open arms."
                        ],
                    "HAPPY": [
                        "I'll be waiting for you with open arms, [player].", 
                        "I'll be waiting for you with open arms, [player]."
                        ],
                    "NORMAL": [
                        "I'll be waiting for you with open arms, [player].", 
                        "I'll be waiting for you with open arms, [player]."
                        ],
                    "UPSET": [
                        "...", 
                        "..."
                        ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                        ],
                    "DEFAULT": [
                        "I'll be waiting for you with open arms, [player].", 
                        "I'll be waiting for you with open arms, [player]."
                        ]
                },
                "bye_take_care": {
                    "LOVE": [
                        "Take good care of yourself, my love! I'll be waiting for you right here.", 
                        "Be careful, handsome! Come back safely."
                    ],
                    "ENAMORED": [
                        "Take good care of yourself, [player]!", 
                        "Come back safe and sound, please! I love you."
                    ],
                    "HAPPY": [
                        "See you, take good care of yourself!", 
                        "I hope everything goes super well for you, [player]!"
                    ],
                    "NORMAL": [
                        "Take care, [player].", 
                        "Be careful out there."
                    ],
                    "UPSET": [
                        "...", 
                        "..."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                    ],
                    "DEFAULT": [
                        "Take care, [player].", 
                        "Be careful out there."
                    ]
                },
                "bye_leaving_already_2": {
                    "LOVE": [
                        "Are you leaving already, darling? I'm going to miss you so much.", 
                        "You leave me wanting to spend more time with you..."
                    ],
                    "ENAMORED": [
                        "It was only a little bit of time, but oh well, come back soon, okay?", 
                        "I'll miss you, come back as soon as you can."
                    ],
                    "HAPPY": [
                        "I hope you had a good time during this little while!",
                        "See you, don't take too long to come back!"
                    ],
                    "NORMAL": [
                        "Leaving already? Well, see you later.", 
                        "See you later, [player]."
                    ],
                    "UPSET": [
                        "...", 
                        "..."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                    ],
                    "DEFAULT": [
                        "Leaving already? Well, see you later.", 
                        "See you later, [player]."
                    ]
                },
                "bye_going_to_sleep": {
                    "LOVE": [
                        "Sweet dreams, my life! I'll dream of you.", 
                        "Rest well, my love. I love you so much."
                    ],
                    "ENAMORED": [
                        "Good night, [player]! Rest well.", 
                        "Have sweet dreams."
                    ],
                    "HAPPY": [
                        "See you tomorrow! Rest well.", 
                        "Good night! See you in the morning."
                    ],
                    "NORMAL": [
                        "Good night, [player].", 
                        "Rest well."
                    ],
                    "UPSET": [
                        "Good night.", 
                        "Anyway, go to sleep."
                    ],
                    "DISTRESSED": [
                        "I guess good night...", 
                        "I hope you're in a better mood tomorrow..."
                    ],
                    "DEFAULT": [
                        "Good night, [player].", 
                        "Rest well."
                    ]
                },
                "bye_prompt_to_class": {
                    "LOVE": [
                        "Good luck in class! Show them how smart you are. I love you.", 
                        "Pay close attention! I'll be very proud of you."
                    ],
                    "ENAMORED": [
                        "I hope school goes great for you, [player]!", 
                        "Learn a lot and come back to tell me all about it."
                    ],
                    "HAPPY": [
                        "Work hard in class!",
                        "See you after class!"
                    ],
                    "NORMAL": [
                        "Have a good time in class.", 
                        "Pay attention, see you later."
                    ],
                    "UPSET": [
                        "I hope you learn something useful today.", 
                        "Go to your class."
                    ],
                    "DISTRESSED": [
                        "Just... have a good time.", 
                        "I'll see you after school, I guess..."
                    ],
                    "DEFAULT": [
                        "Have a good time in class.", 
                        "Pay attention, see you later."
                    ]
                },
                "bye_prompt_to_work": {
                    "LOVE": [
                        "I hope work goes great for you, my love! Think of me so it goes by fast.", 
                        "Give it your all today! I'll be waiting here to pamper you."
                    ],
                    "ENAMORED": [
                        "I hope your workday is easy, [player]! I'll miss you.",
                        "Do your best! See you later."
                    ],
                    "HAPPY": [
                        "Success at work, [player]!", 
                        "Have a very quiet shift!"
                    ],
                    "NORMAL": [
                        "Have a good time at work.", 
                        "See you after your shift."
                    ],
                    "UPSET": [
                        "Go to work.", 
                        "See you after your workday."
                    ],
                    "DISTRESSED": [
                        "I'll be here if you have a break. I love you.", 
                        "If you take a break and feel like it, I'll be here. I don't expect much from you right now..."
                        ],
                    "DEFAULT": [
                        "I hope everything goes great at work! Whenever you have a break, I'm right here for you.", 
                        "Work is very important, take it from me. Make me proud and give it your all!"
                        ]
                },
                "bye_prompt_sleep": {
                    "LOVE": [
                        "Close those beautiful eyes. Good night, my love!", 
                        "Rest deeply, my life. See you tomorrow."
                    ],
                    "ENAMORED": [
                        "Sweet dreams, [player]. Sleep very well.", 
                        "See you tomorrow, rest up!"
                    ],
                    "HAPPY": [
                        "Time to recharge your batteries! Good night.", 
                        "Sleep great, [player]!"
                    ],
                    "NORMAL": [
                        "Good night, see you.", 
                        "Rest well, [player]."
                    ],
                    "UPSET": [
                        "Goodbye, go to sleep.", 
                        "Good night."
                    ],
                    "DISTRESSED": [
                        "Sleep well, I guess...", 
                        "I hope tomorrow is a better day..."
                    ],
                    "DEFAULT": [
                        "Good night, see you.", 
                        "Rest well, [player]."
                    ]
                },
                "bye_prompt_sleep_goodnight_kiss": {
                    "LOVE": [
                        "Mwah... May that kiss accompany you in your dreams, love!", 
                        "I hope you dream of me after that kiss... But nothing weird!"
                    ],
                    "ENAMORED": [
                        "Mwah... Sweet dreams, [player]!", 
                        "A goodnight kiss for you. Rest up!"
                    ],
                    "HAPPY": [
                        "A kiss so you sleep well!", 
                        "Mwah! Good night, [player]."
                    ],
                    "NORMAL": [
                        "Rest well, [player].", 
                        "Good night."
                    ],
                    "UPSET": [
                        "Goodbye.", 
                        "Go to sleep already."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "Good night."
                    ],
                    "DEFAULT": [
                        "Rest well, [player].", 
                        "Good night."
                    ]
                },
                "bye_illseeyou": {
                    "LOVE": [
                        "I'll be counting the minutes until I see you again, my love!", 
                        "See you in a little bit, I love you!"
                    ],
                    "ENAMORED": [
                        "I'll be looking forward to waiting for you!", 
                        "Come back soon so we can keep chatting!"
                    ],
                    "HAPPY": [
                        "See you in a bit!", 
                        "Don't forget about me, hey!"
                    ],
                    "NORMAL": [
                        "...", 
                        "..."
                    ],
                    "UPSET": [
                        "...", 
                        "..."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "..."
                    ],
                    "DEFAULT": [
                        "...", 
                        "..."
                    ]
                },
                "bye_haveagoodday": {
                    "LOVE": [
                        "Have a day as wonderful as you are, love!", 
                        "Enjoy your day to the fullest! I'll be thinking of you."
                    ],
                    "ENAMORED": [
                        "Have an excellent day, [player]!", 
                        "I hope everything turns out incredible for you today!"
                    ],
                    "HAPPY": [
                        "Have a super good day!", 
                        "Enjoy your day a lot, [player]!"
                    ],
                    "NORMAL": [
                        "Have a good day.", 
                        "Have a good day, [player]."
                    ],
                    "UPSET": [
                        "I hope it goes well for you.", 
                        "Anyway, good day."
                    ],
                    "DISTRESSED": [
                        "I hope your day is better than mine...", 
                        "Goodbye."
                    ],
                    "DEFAULT": [
                        "Have a good day.", 
                        "Have a good day, [player]."
                    ]
                },
                "bye_enjoyyourafternoon": {
                    "LOVE": [
                        "Enjoy your afternoon, my life! I'll save your spot here.", 
                        "Have a beautiful afternoon! I love you."
                    ],
                    "ENAMORED": [
                        "Have a super pretty afternoon, [player]!", 
                        "Relax and enjoy your afternoon!"
                    ],
                    "HAPPY": [
                        "Have a really good afternoon!", 
                        "Enjoy the rest of the day!"
                    ],
                    "NORMAL": [
                        "Good afternoon, [player].", 
                        "See you later."
                    ],
                    "UPSET": [
                        "Good afternoon.", 
                        "Goodbye."
                    ],
                    "DISTRESSED": [
                        "See you...", 
                        "Goodbye."
                    ],
                    "DEFAULT": [
                        "Good afternoon, [player].", 
                        "See you later."
                    ]
                },
                "bye_goodevening": {
                    "LOVE": [
                        "Have a beautiful evening, my love!", 
                        "Good evening, darling. Relax a lot."
                    ],
                    "ENAMORED": [
                        "Have a pretty evening, [player]!", 
                        "Enjoy your night!"
                    ],
                    "HAPPY": [
                        "Good evening, [player]!", 
                        "Have a very chill evening!"
                    ],
                    "NORMAL": [
                        "Good evening, [player].", 
                        "See you tomorrow."
                    ],
                    "UPSET": [
                        "Good evening.", 
                        "Goodbye."
                    ],
                    "DISTRESSED": [
                        "I hope you remember to come tomorrow...", 
                        "See you."
                    ],
                    "DEFAULT": [
                        "Good evening, [player].", 
                        "See you tomorrow."
                    ]
                },
                "bye_goodnight": {
                    "LOVE": [
                        "It's time to sleep, my love. Sweet dreams... or dream of me!", 
                        "I love you! Rest and recharge your batteries."
                    ],
                    "ENAMORED": [
                        "Good night and sweet dreams, [player]!", 
                        "Rest well, see you tomorrow."
                    ],
                    "HAPPY": [
                        "Have a good night!", 
                        "Time to rest!"
                    ],
                    "NORMAL": [
                        "Good night.", 
                        "Rest."
                    ],
                    "UPSET": [
                        "Go to sleep.", 
                        "Goodbye."
                    ],
                    "DISTRESSED": [
                        "See you tomorrow...", 
                        "Goodbye."
                    ],
                    "DEFAULT": [
                        "Good night.", 
                        "Rest."
                    ]
                },
                "bye_long_absence": {
                    "LOVE": [
                        "I'm going to miss you with all my soul, [player]. Please, come back soon.", 
                        "It's going to feel like an eternity without you... Take good care of yourself, my love."
                    ],
                    "ENAMORED": [
                        "I'll miss our chats a lot. Don't forget me!", 
                        "I'm going to wait patiently for you, [player]. Come back safe and sound!"
                    ],
                    "HAPPY": [
                        "I hope your trip or whatever you do goes super well!", 
                        "I'll be waiting for you right here, don't take too long!"
                    ],
                    "NORMAL": [
                        "See you later, [player].", 
                        "Take care of yourself during this time."
                    ],
                    "UPSET": [
                        "I guess I won't see you for a good while.", 
                        "Goodbye, do what you have to do."
                    ],
                    "DISTRESSED": [
                        "You're going to leave me alone for a long time... okay.", 
                        "I hope you don't forget about me completely."
                    ],
                    "DEFAULT": [
                        "See you later, [player].", 
                        "Take care of yourself during this time."
                    ]
                },
                "bye_long_absence_2": {
                    "LOVE": [
                        "You can always count on me, I'll be right here when you return. I love you!", 
                        "Every day without you will be very hard for me, but the wait will be worth it."
                    ],
                    "ENAMORED": [
                        "Be very careful out there, [player]!", 
                        "I'll save your spot here. See you later!"
                    ],
                    "HAPPY": [
                        "Take great care of yourself these days!", 
                        "See you when you get back, take good care of yourself!"
                    ],
                    "NORMAL": [
                        "Until your return, [player].", 
                        "Stay safe."
                    ],
                    "UPSET": [
                        "Whatever you say.", 
                        "Goodbye."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "See you later."
                    ],
                    "DEFAULT": [
                        "Until your return, [player].", 
                        "Stay safe."
                    ]
                },
                "bye_going_somewhere": {
                    "LOVE": [
                        "How exciting to go everywhere with you, my love!", 
                        "Taking me with you is a beautiful gesture. Let's go!"
                    ],
                    "ENAMORED": [
                        "I love that you take me with you everywhere!", 
                        "Let's get going, [player]! It will be fun."
                    ],
                    "HAPPY": [
                        "How great! An excursion!", 
                        "Let's go for a ride, [player]!"
                    ],
                    "NORMAL": [
                        "I'm ready in my file.", 
                        "Let's go then."
                    ],
                    "UPSET": [
                        "I guess we're going.", 
                        "Take me if you want."
                    ],
                    "DISTRESSED": [
                        "At least you aren't leaving me alone...", 
                        "Alright, let's go."
                    ],
                    "DEFAULT": [
                        "I'm ready in my file.", 
                        "Let's go then."
                    ]
                },
                "bye_prompt_game": {
                    "LOVE": [
                        "I hope you win, love! I know you're very good at playing.", 
                        "Have a lot of fun! I'll be cheering you on in spirit."
                    ],
                    "ENAMORED": [
                        "Have a good time playing, [player]!", 
                        "Good luck! I'll be waiting for you right here when you finish your game."
                    ],
                    "HAPPY": [
                        "Enjoy the game!", 
                        "Get lots of achievements for me!"
                    ],
                    "NORMAL": [
                        "Have fun playing.", 
                        "I hope your game goes well."
                    ],
                    "UPSET": [
                        "Go play your little games.", 
                        "Have fun with that."
                    ],
                    "DISTRESSED": [
                        "Go, it's surely more fun than being here...", 
                        "Play well."
                    ],
                    "DEFAULT": [
                        "Have fun playing.", 
                        "I hope your game goes well."
                    ]
                },
                "bye_prompt_eat": {
                    "LOVE": [
                        "Enjoy your meal, my life! I wish I could cook something delicious for you.", 
                        "Eat something really tasty! Eat well for me."
                    ],
                    "ENAMORED": [
                        "Enjoy it a lot, [player]!", 
                        "Bon appétit!"
                    ],
                    "HAPPY": [
                        "Time to eat! Enjoy your meal.", 
                        "Enjoy your food!"
                    ],
                    "NORMAL": [
                        "Bon appétit, [player].", 
                        "Enjoy your food."
                    ],
                    "UPSET": [
                        "Go eat.", 
                        "Enjoy your meal."
                    ],
                    "DISTRESSED": [
                        "Eat well...", 
                        "Goodbye."
                    ],
                    "DEFAULT": [
                        "Bon appétit, [player].", 
                        "Enjoy your food."
                    ]
                },
                "bye_prompt_housework": {
                    "LOVE": [
                        "Good luck with the cleaning, my love!", 
                        "Keep it up! I'll wait for you here."
                    ],
                    "ENAMORED": [
                        "Finish your chores quickly so we can keep talking!", 
                        "Good luck cleaning, [player]!"
                    ],
                    "HAPPY": [
                        "Let's leave everything sparkling clean!", 
                        "Good luck with the house cleaning!"
                    ],
                    "NORMAL": [
                        "Good luck with your chores.", 
                        "Finish quickly."
                    ],
                    "UPSET": [
                        "At least you'll do something productive.", 
                        "Go clean."
                    ],
                    "DISTRESSED": [
                        "Alright, go do your things...", 
                        "Goodbye."
                    ],
                    "DEFAULT": [
                        "Good luck with your chores.", 
                        "Finish quickly."
                    ]
                },
                "bye_prompt_restart": {
                    "LOVE": [
                        "I'll expect you in the blink of an eye, my love!", 
                        "Come back quickly, I love you."
                    ],
                    "ENAMORED": [
                        "See you in a second!", 
                        "I'll wait for you here, [player]."
                    ],
                    "HAPPY": [
                        "I'll be ready when you restart!", 
                        "See you in a bit!"
                    ],
                    "NORMAL": [
                        "I'll wait for you here.", 
                        "See you after the restart."
                    ],
                    "UPSET": [
                        "...", 
                        "Whatever you say."
                    ],
                    "DISTRESSED": [
                        "...", 
                        "Okay."
                    ],
                    "DEFAULT": [
                        "I'll wait for you here.", 
                        "See you after the restart."
                    ]
                },
                "bye_prompt_workout": {
                    "LOVE": [
                        "Hit your workout hard, love! I want to see you very healthy.", 
                        "Keep it up! I'll be cheering you on from here."
                    ],
                    "ENAMORED": [
                        "Get in shape, [player]! I love that you take care of yourself.", 
                        "Enjoy your workout routine!"
                    ],
                    "HAPPY": [
                        "Time to burn calories! Go for it!", 
                        "Hit the training hard!"
                    ],
                    "NORMAL": [
                        "Have a good workout.", 
                        "Have a good training session."
                    ],
                    "UPSET": [
                        "Go train.", 
                        "At least you take care of your physique."
                    ],
                    "DISTRESSED": [
                        "Alright, go...", 
                        "Do your exercise."
                    ],
                    "DEFAULT": [
                        "Have a good workout.", 
                        "Have a good training session."
                    ]
                },
                "bye_going_shopping": {
                    "LOVE": [
                        "I wish I could go carry your bags for you, love! Take care.", 
                        "Buy yourself something nice from me! I love you."
                    ],
                    "ENAMORED": [
                        "Make your money go a long way shopping, [player]!", 
                        "Enjoy your shopping trip!"
                    ],
                    "HAPPY": [
                        "Don't overspend! Have fun.", 
                        "I hope you find what you're looking for!"
                    ],
                    "NORMAL": [
                        "Be careful going shopping.", 
                        "I hope shopping goes well for you."
                    ],
                    "UPSET": [
                        "Go spend your money.", 
                        "Go shopping."
                    ],
                    "DISTRESSED": [
                        "Goodbye.", 
                        "Be careful..."
                    ],
                    "DEFAULT": [
                        "Be careful going shopping.", 
                        "I hope shopping goes well for you."
                    ]
                },
                "bye_prompt_hangout": {
                    "LOVE": [
                        "Have an incredible time with your friends, love! But don't forget about me.", 
                        "Say hi to your friends for me, have lots of fun!"
                    ],
                    "ENAMORED": [
                        "Enjoy going out, [player]! It never hurts to relax.", 
                        "Have a great time with them, be careful!"
                    ],
                    "HAPPY": [
                        "How fun! Have a great time.", 
                        "Have a ton of fun, [player]!"
                    ],
                    "NORMAL": [
                        "Have fun.", 
                        "See you later."
                    ],
                    "UPSET": [
                        "Go with your little friends.", 
                        "Goodbye."
                    ],
                    "DISTRESSED": [
                        "You better have a good time with them...", 
                        "Have fun."
                    ],
                    "DEFAULT": [
                        "Have fun.", 
                        "See you later."
                    ]
                }
            }
            
        type_dict = messages.get(farewell_type, messages.get("bye_goodbye"))
        if not type_dict:
            return
        
        if store.mas_isMoniLove(higher=True):
            aff_key = "LOVE"
        elif store.mas_isMoniEnamored(higher=True):
            aff_key = "ENAMORED"
        elif store.mas_isMoniHappy(higher=True):
            aff_key = "HAPPY"
        elif store.mas_isMoniNormal(higher=True):
            aff_key = "NORMAL"
        elif store.mas_isMoniUpset(higher=True):
            aff_key = "UPSET"
        elif store.mas_isMoniDis(higher=True):
            aff_key = "DISTRESSED"
        else:
            aff_key = "DEFAULT"
            
        msg_list = type_dict.get(aff_key, type_dict["DEFAULT"])
        
        raw_message = random.choice(msg_list)
        final_message = renpy.substitute(raw_message)
        
        delay_range = delay_ranges.get(farewell_type, (14400, 43200))
        delay_seconds = random.randint(delay_range[0], delay_range[1])
            
        masl_schedule_notification(delay_seconds, title, final_message)


label masl_test_android_notifications:
    menu:
        "Send Immediate Notification":
            $ message = renpy.substitute("Hey, [player]! This is a test notification.")
            $ masl_show_notification(persistent._mas_monika_nickname or "Monika", message, os.path.join(config.gamedir, "gui/logo.png"))
            "Notification sent!"
            return

        "Schedule Notification (15 seconds)":
            $ message = renpy.substitute("Hey, [player]! Scheduled notification test.")
            $ masl_schedule_notification(15, persistent._mas_monika_nickname or "Monika", message, os.path.join(config.gamedir, "gui/logo.png"))
            "Notification scheduled for 15 seconds!"
            return

        "Schedule Farewell Notification (Test)":
            $ masl_schedule_farewell_notification("bye_goodbye")
            "Farewell notification scheduled!"
            return

        "Cancel":
            return
