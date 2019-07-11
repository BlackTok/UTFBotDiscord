import discord, asyncio, sql


author = (
    'Admin',)

def send_message():
    print("Бот запущен")
    client = discord.Client()
    
    @client.event
    async def on_ready():
        while True:
            data = sql.connect_sql()

            if data[1] == '1':
                sql.update_sql()
                comander = data[10]

                for i in [11,12,13]:
                    if data[i] != '':
                        comander = comander + data[i]

                message = ":earth_africa:\n\nОкрестности :fire: {0} :fire:  в огне!\nВ результате операции город был освобождён от противника!\n\nПротивник понёс потери:\n:one: Пехота - {1}\n:two: Легкая техника - {2}\n:three: Бронированная техника - {3}\n:four: Воздушная техника - {4}\n\n:white_check_mark: В освобождении города участвовали {5} бойцов под командованием {6}\n\nПотери нашей стороны:\n:wheelchair: легких ранений - {7}\n:skull_crossbones:️ убитых - {8}\n\nРезультаты операции в городе {9} отправлены в штаб :pencil:".format(data[7],data[2],data[3],data[4],data[5],data[9],comander,data[6],data[14],data[7])
                print("Искра обновилась!")
                ch = client.get_channel(519599823247114245)
                await ch.send(message)

            await asyncio.sleep(10)


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        #личный состав
        if message.content.startswith('!лс список'):
            authorM = message.author
            if str(authorM) in author:
                plist = sql.getListPlayers()
                msg = '___Имя - Статус - Комментарий___'
                for i in plist:
                    msg = msg + f'\n___{i[0]} - {i[1]} - {i[3]} - {i[4]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')
        
        if message.content.startswith('!лс обновить'):
            authorM = message.author
            if str(authorM) in author:
                sql.getListUpdate()
                await message.channel.send('Список обновлен')
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!лс пропажа'):
            authorM = message.author
            if str(authorM) in author:
                offline = sql.getListPropaga()
                if len(offline) > 0:
                    for i in offline:
                        msg1 = f'Игрок {i[0]} не был в онлайне больше месяца'
                        await message.channel.send(msg1)
                else:
                    await message.channel.send('Пропаж не найдено')
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!лс изменить'):
            authorM = message.author
            if str(authorM) in author:
                msgA = message.content
                spl = (msgA.split('.'))[1:]
                if len(spl) == 3:
                    param_1 = spl[0]
                    param_2 = spl[1]
                    param_3 = spl[2]
                    sql.updateRow(param_1,param_2,param_3)
                    await message.channel.send('Игрок изменен')                                 
                else:
                    await message.channel.send('Команда не верна')
            else:
                await message.channel.send('У вас нет прав')



        #зевсы
        if message.content.startswith('!зевс список'):
            authorM = message.author
            if str(authorM) in author:
                zlist = sql.getListZeus()
                msg = '___Имя - Статус - Комментарий___'
                for i in zlist:
                    msg = msg + f'\n___{i[0]} - {i[1]} - {i[2]} - {i[3]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!зевс добавить'):
            authorM = message.author
            if str(authorM) in author:
                msgA = message.content
                spl = (msgA.split('.'))[1:]
                if len(spl) == 3:
                    param_1 = spl[0]
                    param_2 = spl[1]
                    param_3 = spl[2]
                    sql.addRowZeus(param_1,param_2,param_3)
                    await message.channel.send('Зевс добавлен')
                else:
                    await message.channel.send('Команда не верна')
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!зевс изменить'):
            authorM = message.author
            if str(authorM) in author:
                msgA = message.content
                spl = (msgA.split('.'))[1:]
                if len(spl) == 3:
                    param_1 = spl[0]
                    param_2 = spl[1]
                    param_3 = spl[2]
                    result = sql.updateRowZeus(param_1,param_2,param_3)
                    if result:
                        await message.channel.send('Зевс изменен')
                    else:
                        await message.channel.send('Зевс не найден')
                else:
                    await message.channel.send('Команда не верна')
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!зевс -'):
            authorM = message.author
            if str(authorM) in author:
                msgA = message.content
                spl = (msgA.split('.'))[1:]
                result = sql.minusScoreZeus(spl[0])
                await message.channel.send(f'Зевс {result[0]} наказан')
                if result[1]:
                    await message.channel.send(f'Зевс {result[0]} рекомендуется к отстранению')
            else:
                await message.channel.send('У вас нет прав')



        #пилоты
        if message.content.startswith('!пилоты список'):
            authorM = message.author
            if str(authorM) in author:
                result = sql.pilotSpisok()
                msg = '___Пилот - Допуск___'
                for i in result:
                    msg = msg + f'\n___{i[0]} - {i[1]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')
                
        if message.content.startswith('!пилоты 2'):
            authorM = message.author
            if str(authorM) in author:
                result = sql.pilot2()
                msg = '___Пилот - Допуск___'
                for i in result:
                    msg = msg + f'\n___{i[0]} - {i[1]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!пилоты 3'):
            authorM = message.author
            if str(authorM) in author:
                result = sql.pilot3()
                msg = '___Пилот - Допуск___'
                for i in result:
                    msg = msg + f'\n___{i[0]} - {i[1]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')

        if message.content.startswith('!пилоты 4'):
            authorM = message.author
            if str(authorM) in author:
                result = sql.pilot4()
                msg = '___Пилот - Допуск___'
                for i in result:
                    msg = msg + f'\n___{i[0]} - {i[1]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')



        #зеленые
        if message.content.startswith('!бс список'):
            authorM = message.author
            if str(authorM) in author:
                result = sql.greenSpisok()
                msg = '___БС___'
                for i in result:
                    msg = msg + f'\n___{i[0]}___'
                await message.channel.send(msg)
            else:
                await message.channel.send('У вас нет прав')

    client.run('TOKEN')


def main():
    send_message()


if __name__ == "__main__":
    main()