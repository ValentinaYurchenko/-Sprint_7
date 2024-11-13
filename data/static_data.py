
class OrderData:
    data = {
        'firstname': "Naruto",
        'lastname': 'Uchiha',
        'address': 'Konoha',
        'metroStation': 4,
        'phone': '+7 800 355 35 35',
        'rentTime': 5,
        'deliveryDate': '2020-06-06',
        'comment': 'Saske, come back to Konoha'
    }


class ResponseData:
    courier_successful_response = '{"ok":true}'
    same_login = 'Этот логин уже используется'
    not_enough_reg_data_response = 'Недостаточно данных для создания учетной записи'
    invalid_id_response = 'Курьера с таким id нет'
    null_id_response = 'invalid input syntax'
    track_in_order_list = "track"
    profile_404_response = 'Учетная запись не найдена'
    not_enough_login_data_response = 'Недостаточно данных для входа'
