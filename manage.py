# coding: utf-8
import pygame
import pygame.camera
from pygame.locals import *
from settings import api
import sys
class Photographer(object):
    def __init__(self,camera_port = "/dev/video0"):
        pygame.init()
        pygame.camera.init()
        self.cam = pygame.camera.Camera(camera_port,(640,480))

    def take_a_pic(self,filename = 'pic.jpg'):
        self.cam.start()
        image = self.cam.get_image()
        pygame.image.save(image,filename)
        self.filename = filename

    def post_a_pic(self,comment,hastag = u'#asahikawa_python'):
        photo = open(self.filename,'rb')
        if len(comment+hastag) > 139:
            print 'your tweet is beyond 140 characters which'
            ' is the limitation of tweet.\n please tweet again'
            return None
        api.update_status_with_media(media=photo,
                status=u'{comment} {hastag}'.format(
                    comment = comment,
                    hastag = hastag
                    ))

    def tweet(self,comment,hastag = u'#asahikawa_python',
            filename = 'pic.jpg'):
        self.take_a_pic(filename)
        self.post_a_pic(comment,hastag)

def main(*argv):
    Rpi = Photographer()
    if len(argv) == 3:
        Rpi.tweet(comment = argv[0][1],
                hastag = argv[0][2])
    elif len(argv) == 2:
        Rpi.tweet(comment = argv[0][1])

if __name__ == '__main__':
    main(sys.argv)


