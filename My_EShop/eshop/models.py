from django.db import models
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from My_EShop.core.validators import validate_max_image_size


class Brand(models.Model):
    BRAND_TITLE_MAX_LEN = 100
    BRAND_DESCRIPTION_MAX_LEN = 300

    title = models.CharField(
        max_length=BRAND_TITLE_MAX_LEN,
    )
    image = models.ImageField(upload_to='images/brand_img')
    intro_text = models.CharField(
        max_length=BRAND_DESCRIPTION_MAX_LEN,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Category(MPTTModel):
    CATEGORY_TITLE_MAX_LEN = 50
    SLUG_MAX_LEN = 50

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    title = models.CharField(
        max_length=CATEGORY_TITLE_MAX_LEN,
    )

    # null=False, blank=True, if we don't write slug ,automatically to be 'null' and 'save'
    slug = models.SlugField(
        max_length=SLUG_MAX_LEN,
        unique=True,
        null=False,
        blank=True,
    )
    category_image = models.ImageField(
        upload_to='categories/',
        null=True,
        blank=True,
        validators=(
            validate_max_image_size,
        ),
    )
    category_banner_image = models.ImageField(
        upload_to='categories/',
        null=True,
        blank=True,
        validators=(
            validate_max_image_size,
        ),
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        # create/update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}')

        # update
        return super().save(*args, **kwargs)

    # @staticmethod
    # def get_all_categories():
    #     return Category.objects.all()

    def __str__(self):
        full_path = [self.title]
        sub_cat = self.parent
        while sub_cat is not None:
            full_path.append(sub_cat.title)
            sub_cat = sub_cat.parent
        return ' / '.join(full_path[::-1])


class Product(models.Model):
    PRODUCT_NAME_MAX_LEN = 150
    PRODUCT_DESCRIPTION_MAX_LEN = 400

    name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LEN,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1,
    )

    price = models.PositiveIntegerField(default=0)
    discounted_price = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=PRODUCT_DESCRIPTION_MAX_LEN,
        default='',
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='images/products',
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    in_stock = models.BooleanField(default=True)

    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # @property
    # def get_featured_image(self):
    #     image = self.images.filter(is_featured=True).first()
    #     return image.image.url if image else None
    #
    # @property
    # def get_price(self):
    #     if self.discounted_price:
    #         return self.discounted_price
    #     return self.price



# Color
# class Color(models.Model):
#     title=models.CharField(max_length=100)
#     color_code=models.CharField(max_length=100)
#
#     def color_bg(self):
#         return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))
#
#     def __str__(self):
#         return self.title

# Size
# class Size(models.Model):
#     title=models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title

# class ProductAttribute(models.Model):
#
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     color = models.ForeignKey(Color,on_delete=models.CASCADE)
#     size = models.ForeignKey(Size,on_delete=models.CASCADE)
#     price = models.PositiveIntegerField(default=0)
#     image = models.ImageField(upload_to="product_imgs/", null=True)

# class Order(models.Model):
#     STATUS = (
#         ('Pending', 'Pending'),
#         ('Order Confirmed', 'Order Confirmed'),
#         ('Out for Delivery', 'Out for Delivery'),
#         ('Delivered', 'Delivered'),
#     )
#
#     # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     email = models.CharField(max_length=50, null=True)
#     address = models.CharField(max_length=500, null=True)
#     mobile = models.CharField(max_length=20, null=True)
#     order_date = models.DateField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=50, null=True, choices=STATUS)

# Order
# status_choice=(
#         ('process','In Process'),
#         ('shipped','Shipped'),
#         ('delivered','Delivered'),
#     )
# class CartOrder(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     total_amt=models.FloatField()
#     paid_status=models.BooleanField(default=False)
#     order_dt=models.DateTimeField(auto_now_add=True)
#     order_status=models.CharField(choices=status_choice,default='process',max_length=150)
#
#     class Meta:
#         verbose_name_plural='8. Orders'
#
# # OrderItems
# class CartOrderItems(models.Model):
#     order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
#     invoice_no=models.CharField(max_length=150)
#     item=models.CharField(max_length=150)
#     image=models.CharField(max_length=200)
#     qty=models.IntegerField()
#     price=models.FloatField()
#     total=models.FloatField()
#
#     class Meta:
#         verbose_name_plural='9. Order Items'
#
#     def image_tag(self):
#         return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
#
# # Product Review
# RATING=(
#     (1,'1'),
#     (2,'2'),
#     (3,'3'),
#     (4,'4'),
#     (5,'5'),
# )
# class ProductReview(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     review_text=models.TextField()
#     review_rating=models.CharField(choices=RATING,max_length=150)
#
#     class Meta:
#         verbose_name_plural='Reviews'
#
#     def get_review_rating(self):
#         return self.review_rating
#
# # WishList
# class Wishlist(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural='Wishlist'
