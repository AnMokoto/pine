

# @python_2_unicode_compatible
# class Upload(models.Model, ToString):
#     name = models.TextField(verbose_name=u"文件类型")
#
#
# @python_2_unicode_compatible
# class UploadImage(models.Model, ToString):
#     name = models.TextField(verbose_name=u"图片")
#     image = models.ImageField(upload_to='images/upload/%Y/%m/%d/', )
#     type = models.ForeignKey(Upload, on_delete=models.CASCADE)
#
#
# @python_2_unicode_compatible
# class UploadFile(models.Model, ToString):
#     name = models.TextField(verbose_name=u"文件")
#     image = models.FileField(upload_to='files/upload/%Y/%m/%d/')
#     type = models.ForeignKey(Upload, on_delete=models.CASCADE)

