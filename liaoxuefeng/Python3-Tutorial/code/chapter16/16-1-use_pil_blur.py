#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

# ��һ��jpgͼ���ļ���ע���ǵ�ǰ·��:
im = Image.open('test.jpg')
# Ӧ��ģ���˾�:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')