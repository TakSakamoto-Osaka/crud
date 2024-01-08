from typing import Any
from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Product

class Command(BaseCommand):
    help = "テストコマンド"

    @transaction.atomic
    def handle(self, *args: Any, **options: Any):
        print('テスト')
        
        prd = Product(name='ラジオ', price=10000)
        prd.save()
       
        prd = Product(name='ビデオ', price=30000)
        prd.save()
        

