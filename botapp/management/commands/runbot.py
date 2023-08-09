from django.core.management.base import BaseCommand

from ...loader import bot

class Command(BaseCommand):
    help = 'Botni ishga tushirish...'

    def handle(self, *args, **options):
        from ... import handlers
        print('Bot ishga tushdi...')
        bot.infinity_polling()


