from django.db import models


class Wheel(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_wheel'


class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_nav'


class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mustbuy'


class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_shop'


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'


class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    typesort = models.IntegerField()
    childtypenames = models.CharField(max_length=150)

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=50)
    productlongname = models.CharField(max_length=100)
    isxf = models.NullBooleanField(default=False)
    pmdesc = models.CharField(max_length=10)
    specifics = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    marketprice = models.CharField(max_length=10)
    categoryid = models.CharField(max_length=10)
    childcid = models.CharField(max_length=10)
    childcidname = models.CharField(max_length=10)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'axf_user'


class Order(models.Model):
    orderUser = models.ForeignKey(User)
    orderInfo = models.CharField(max_length=1000)
    orderFlag = models.CharField(max_length=20,default='cart')

    class Meta:
        db_table = 'axf_order'