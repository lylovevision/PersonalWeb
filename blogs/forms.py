# -*- coding: utf-8 -*-
__author__ = 'bobby'

import re
from django import forms

from blogs.models import Contact


class Contact(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['pen_name', 'email', 'conten']