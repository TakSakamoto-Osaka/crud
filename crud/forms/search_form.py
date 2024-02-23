from django.forms import Form, CharField

class SearchForm(Form):
    shop_name = CharField(max_length=100, label = '店名')
    genre = CharField(label='ジャンル')