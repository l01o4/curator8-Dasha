import telebot

bot = telebot.TeleBot('6693389876:AAGGBbV9vleWAD3F7_Mh65YOjl_mCqJBaCU')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет')


@bot.message_handler(commands=['first'])
def main(message):
    bot.send_message(message.chat.id,
                     'первое универсальное произведение для ИС - Гоголь "Мертвые души". Краткое содержание:Книга рассказывает о похождениях Чичикова Павла Ивановича, главного героя рассказа, бывшего коллежского советника, выдающего себя за помещика. Чичиков приезжает в конкретно неназванный городок, некий губернский «город N» и немедленно пытается войти в доверие ко всем сколько-либо важным обитателям города, что ему успешно удаётся. Герой становится крайне желанным гостем на балах и обедах. Горожане неназванного города не догадываются об истинных целях Чичикова. А цель его заключается в скупке или безвозмездном приобретении умерших крестьян, которые по переписи ещё числились как живые у местных помещиков, и последующем оформлении их на своё имя как живых. О характере, прошлой жизни Чичикова и о его дальнейших намерениях насчёт «мёртвых душ» рассказывается в последней, одиннадцатой главе. Чичиков любыми способами пытается разбогатеть, добиться высокого социального статуса. В прошлом Чичиков служил в таможне, за взятки позволял контрабандистам беспрепятственно переправлять товары через границу. Однако поссорился с подельником, тот написал на него донос, после чего афера раскрылась, и оба оказались под следствием. Подельник попал в тюрьму, а Чичиков, чтобы не быть пойманным, немедленно покинул губернию. При этом он не забрал денег из банка, успев взять с собой только несколько рубашек, немного казенной бумаги, да пару кусков мыла.')


@bot.message_handler(commands=['second'])
def main(message):
    bot.send_message(message.chat.id,
                     'Тургенев "Отцы и Дети".Молодой человек, сын помещика, вернулся домой после учёбы и привёз с собой друга, Базарова.Евгений Васильевич Базаров — убеждённый нигилист, студент-медик, высокий, светловолосый, с длинным, худым лицом и бакенбардами, зеленоватыми глазами, умный, спокойный, самоуверенный.Базаров ни во что не верил, никого не уважал и быстро восстановил против себя старшее поколение.Через некоторое время, благодаря богатому родственнику, друзья попали на бал к губернатору, где познакомились с молодой красивой вдовой и влюбились в неё. Вдова пригласила друзей в своё богатое поместье. Там она увлеклась Базаровым, а сын помещика сблизился с её младшей сестрой.Базаров не верил в любовь и испугался этого чувства, а вдова не захотела рисковать своим покоем. Они расстались. Друзьям пришлось уехать. Они погостили у родителей нигилиста, затем сын помещика, не терявший надежды покорить вдову, вернулся в её поместье.Базаров отправился в поместье друга и начал ухаживать за молодой сожительницей помещика. Брат помещика, тайно влюблённый в сожительницу, узнал об этом, вызвал Базарова на дуэль, и тот ранил его в ногу.После дуэли Базарову пришлось уехать. Он заехал к вдове, примирился с ней и узнал, что сын помещика влюблён в её сестру. Базаров понял, что их пути расходятся, и расстался с другом навсегда. Он вернулся к родителям, начал лечить крестьян и умер, заразившись тифом. Перед смертью он успел попрощаться с вдовой.Вскоре вдова вышла замуж по расчёту. Сын помещика женился на её сестре, помещик обвенчался с сожительницей, а его брат навсегда уехал в Европу. ')


@bot.message_handler(commands=['third'])
def main(message):
    bot.send_message(message.chat.id,
                     'Островский гроза.19-й век. Небольшой городок на Волге. Свекровь Катерины была вдовой и богатой купчихой.Катерина Кабанова — молодая, красивая, робкая и кроткая, честная, безвольная, много молится, страдает от тирании свекрови.Муж Катерины полностью подчинялся властной и жестокой матери, и та всячески тиранила и сына, и его несчастную жену.Катерина полюбила племянника жестокого и жадного купца, жившего в том же городке. Когда муж Катерины уехал из городка по делам, женщина начала встречаться с племянником купца.Когда муж вернулся, Катерина не выдержала мук совести и призналась ему в измене. После этого свекровь стала ещё сильнее тиранить женщину.Вскоре племяннику купца пришлось уехать: дядя отправил его в Сибирь. Взять с собой Катерину он не мог, потому что полностью зависел от дяди. Распрощавшись с любимым, Катерина поняла, что не сможет вернуться в дом к мужу и свекрови, бросилась с обрыва в Волгу и погибла.')


bot.infinity_polling()
