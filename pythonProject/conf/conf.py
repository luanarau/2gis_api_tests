BASE_URL_2_0 = 'https://catalog.api.2gis.com/2.0/'
BASE_URL_3_0 = 'https://catalog.api.2gis.com/3.0/'

KEY = 'e7f5231f-6951-449a-8ba4-bbefe834b54a'

STATUSCODES = [200, 400, 403, 404, 408, 500]

test_city_valid_data = ['Новосибирск', 'Moscow', 'Юрга', 'Кемерово', 'Ереван']
test_city_invalid_data = ['-1', 'New York', 'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch', 'Å']
test_valid_query = ['No spicy please', 'Сан Сити', 'НГТУ', 'Речной вокзал']

test_city_valid_json_responce = {'Новосибирск': [{
                                                "full_name": "Новосибирск",
                                                "id": "141360258613345",
                                                "name": "Новосибирск",
                                                "subtype": "city",
                                                "type": "adm_div"
                                            },
                                            {
                                                "address_name": "Гоголя street, 13",
                                                "building_name": "Галерея Новосибирск, торгово-развлекательный центр",
                                                "full_name": "Новосибирск, Галерея Новосибирск, торгово-развлекательный центр",
                                                "id": "70000001007536870",
                                                "name": "Галерея Новосибирск, торгово-развлекательный центр",
                                                "purpose_name": "Shopping and entertainment complex",
                                                "type": "branch"
                                            },
                                            {
                                                "address_name": "Дмитрия Шамшурина, 43",
                                                "building_name": "Новосибирск-Главный, железнодорожный вокзал",
                                                "full_name": "Новосибирск, Новосибирск-Главный, железнодорожный вокзал",
                                                "id": "141265769369926",
                                                "name": "Новосибирск-Главный, железнодорожный вокзал",
                                                "purpose_name": "Вокзал",
                                                "type": "branch"
                                            }],

                                    'Moscow': [{
                                            "full_name": "Москва",
                                            "id": "4504222397630173",
                                            "name": "Москва",
                                            "subtype": "city",
                                            "type": "adm_div"
                                        },
                                        {
                                            "full_name": "Moscow",
                                            "id": "5349042514588558",
                                            "name": "Moscow",
                                            "subtype": "region",
                                            "type": "adm_div"
                                    }],
                                    'Юрга': [{
                                            "full_name": "Yurga",
                                            "id": "70030076138465544",
                                            "name": "Yurga",
                                            "subtype": "city",
                                            "type": "adm_div"
                                    }],
                                    'Кемерово': [
                                        {
                                            "full_name": "Кемерово",
                                            "id": "704310212034621",
                                            "name": "Кемерово",
                                            "subtype": "city",
                                            "type": "adm_div"
                                        },
                                        {
                                            "full_name": "Кемерово",
                                            "id": "704473420792427",
                                            "name": "Кемерово",
                                            "route_type": "suburban_train",
                                            "subtype": "railway",
                                            "type": "station"
                                        }
                                    ],
                                    'Ереван': [
                                            {
                                                "full_name": "Yerevan",
                                                "id": "70030076174472031",
                                                "name": "Yerevan",
                                                "subtype": "city",
                                                "type": "adm_div"
                                            },
                                            {
                                                "address_comment": "1 этаж",
                                                "address_name": "Екатерининская, 30",
                                                "id": "70000001036936621",
                                                "name": "Ереван, кафе",
                                                "type": "branch"
                                            },
                                            {
                                                "address_name": "Большая Тульская street, 13",
                                                "building_name": "Ереван Плаза, торгово-развлекательный центр",
                                                "full_name": "Москва, Ереван Плаза, торгово-развлекательный центр",
                                                "id": "4504127908391840",
                                                "name": "Ереван плаза, торгово-развлекательный центр",
                                                "purpose_name": "Shopping and entertainment complex",
                                                "type": "branch"
                                            },
                                            {
                                                "address_name": "Кирова, 42",
                                                "building_name": "Ереван, бизнес-центр",
                                                "full_name": "Пенза, Ереван, бизнес-центр",
                                                "id": "70000001026729373",
                                                "name": "Ереван, бизнес-центр",
                                                "purpose_name": "Business center",
                                                "type": "branch"
                                            },
                                            {
                                                "address_comment": "цокольный этаж",
                                                "address_name": "Кирова, 42",
                                                "id": "5911502791908024",
                                                "name": "Ереван, ресторан",
                                                "type": "branch"
                                            },
                                            {
                                                "full_name": "Yerevan",
                                                "id": "70030076149053871",
                                                "name": "Yerevan",
                                                "subtype": "region",
                                                "type": "adm_div"
                                            },
                                        ]}