@logger.catch
def get_data_wires(self, wire_number):
    staitment = select(Wires).where(Wires.name.in_([wire_number]))
    try:
        wire = self.session.scalar(staitment).description
        return wire
    except AttributeError:
        print('Недопустимое значение')
        return None


@logger.catch
def wires(self, message) -> None:
    """
    Обрабатывает запрос от пользователя,
    связывается с БД (табличка 'Провода'),
    отпровляет данные с БД (описание провода).
    """
    wire_number = message.text
    wire = self.accessData.get_data_wires(wire_number)
    if wire is not None:
        self.bot.send_message(message.chat.id, wire)
    else:
        self.bot.send_message(message.chat.id,
                              'Такого провода нет.\n'
                              'В базе есть провода с 1-71.')

@logger.catch
def get_data_devices(self, user, deviсe_name):
    staitment = select(
        user).where(user.name.in_([deviсe_name]))
    try:
        dev_des = self.session.scalar(staitment).description
        dev_loc = self.session.scalar(staitment).location
        return [dev_des, dev_loc]
    except AttributeError:
        print('Недопустимое значение')
        return None

@logger.catch
def devices_in_cabinets(self, message) -> None:
    """
    Обрабатывает запрос от пользователя,
    связывается с БД (таблички данного типа вагона),
    отпровляет данные с БД (описание конкретного аппарата).
    """
    user = self.temp_data[message.chat.id]
    deviсe_name = message.text.upper()
    dev_des, dev_loc = self.dataAccess.get_data_devices(user, deviсe_name)
    if dev_des and dev_loc is not None:
        self.bot.send_message(
                message.chat.id,
                f'Находится: {dev_loc}\n{dev_des}')
    else:
        self.bot.send_message(
                message.chat.id,
                'Такого аппарата в данном вагоне нет.\n'
                'Или проверьте правильность написания.\n'
                'Пишите название через тире.\n'
                'Пример: Тр-7, ПР-10, КЛП-О, АВУ')


@logger.catch
def fuses_in_cabinets(self, message) -> None:
    """
    Обрабатывает запрос от пользователя,
    связывается с БД (табличка данного типа вагона),
    отпровляет данные с БД (все предохранители в шкафу).
    """
    tablet = self.temp_data[message.chat.id][0]
    cabinet = self.temp_data[message.chat.id][1]
    all_fuses = self.dataAccess.get_data_fuses(tablet, cabinet)
    self.bot.send_message(message.chat.id, '----------------------------')
    self.bot.send_message(message.chat.id, all_fuses)


@logger.catch
def get_data_fuses(self, tablet, cabinet):
    staitment = select(
        tablet).where(
        tablet.location.in_(
            [cabinet])).filter(
                tablet.name.like('ПР-%'))
    all_fuses = []
    for fuses in self.session.scalars(staitment):
        all_fuses.append(f'{fuses.name}: {fuses.description.lower()}\n')
    return all_fuses
