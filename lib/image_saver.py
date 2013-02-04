# -*- coding: utf-8 -*-

import os

from lib.common import log


def save(image_object, image_file, img_format='PNG'):
    ''' tries to save image object as file
    @param image_object: Image.Image object
    @param image_file: string
    @param img_format: string (default='PNG')
    @return boolean

    image_file can be absolute or relative path

    usage: save(image_object, '/where/to/save/image/img')
    returns True or False on error'''
    path = os.path.abspath(image_file)

    try:
        image_object.save(path, format=img_format)

        return True

    except Exception, e:
        log.error('Error while saving image file: %s, error was: %r' % (path, e))
        return False
