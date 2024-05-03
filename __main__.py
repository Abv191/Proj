from Bot import Bot
from ui import ConsoleUserInterface

if __name__ == "__main__":
    ui = ConsoleUserInterface()
    ui.display_message('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot(ui)
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = ui.get_input('Type help for list of commands or enter your command\n')
        if action == 'help':
            format_str = str('{:%s%d}' % ('^',20))
            for command in commands:
                ui.display_message(format_str.format(command))
            action = ui.get_input()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break

