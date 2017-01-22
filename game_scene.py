# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import time
import sound
import json


#pillar_x = 100
#pillar_y = 400

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.high_score = 0
        
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/game.PNG', 
                                 parent = self, 
                                 size = self.size,
                                 position = self.size/2)
                                 
        self.character_position = Vector2(self.size_of_screen_x * 0.2, self.size_of_screen_y * 0.5)
        self.character = SpriteNode('assets/sprites/alien.png',
                                    parent = self,
                                    position = self.character_position)
                                    #scale = 0.1)
                                    
        
        button_position = Vector2(self.size_of_screen_x * 0.1, self.size_of_screen_y * 0.1)
        self.play_button = SpriteNode('assets/sprites/instructions_button.PNG',
                                 parent = self,
                                 position = button_position,
                                 scale = 12,
                                 alpha = 0.0)
                                 
        self.menu_button = SpriteNode('assets/sprites/menu.png',
                                          parent = self,
                                          position = self.size/2,
                                          scale = 0.5,
                                          alpha = 0.0)
                                          
        bottom_pillar_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y - 60)
        self.pillar_bottom = SpriteNode('assets/sprites/IMG_6446.PNG',
                                        parent = self,
                                        position = bottom_pillar_position,
                                        scale = 0.75,
                                        size = (self.size_of_screen_x*0.2, self.size_of_screen_y*0.75))
                                        
        score_pillar_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y/2)
        self.score_bottom = SpriteNode('assets/sprites/IMG_6446.PNG',
                                        parent = self,
                                        position = score_pillar_position,
                                        scale = 0.75,
                                        size = (self.size_of_screen_x*0.2, self.size_of_screen_y*0.75),
                                        alpha = 0.0)
                                        
        top_pillar_position = Vector2(self.size_of_screen_x * 0.5, 60)
        self.pillar_top = SpriteNode('assets/sprites/IMG_6446.PNG',
                                        parent = self,
                                        position = top_pillar_position,
                                        scale = 0.75,
                                        size = (self.size_of_screen_x*0.2, self.size_of_screen_y*0.75))
                                        
                                        
        left_side_border_postion = Vector2(self.size_of_screen_x, self.size_of_screen_y)
        self.left_side_border = SpriteNode('assets/sprites/side_borders.PNG',
                                           parent = self,
                                           position = left_side_border_postion,
                                           size = (self.size_of_screen_x/10, self.size_of_screen_y*2))
                                           
        right_side_border_postion = Vector2(0, self.size_of_screen_y)
        self.right_side_border = SpriteNode('assets/sprites/side_borders.PNG',
                                           parent = self,
                                           position = right_side_border_postion,
                                           size = (self.size_of_screen_x/10, self.size_of_screen_y*2))
                                           
        bottom_border_postion = Vector2(self.size_of_screen_x * 0.5, 0)
        self.bottom_border = SpriteNode('assets/sprites/top_and_bottom.PNG',
                                        parent = self,
                                        position = bottom_border_postion,
                                        size = (self.size_of_screen_x*2, self.size_of_screen_y/10))
                                      
        top_border_postion = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y)
        self.top_border = SpriteNode('assets/sprites/top_and_bottom.PNG',
                                        parent = self,
                                        position = top_border_postion,
                                        size = (self.size_of_screen_x*2, self.size_of_screen_y/10))
                                        
        score_label_position = Vector2(self.size_of_screen_x/6, self.size_of_screen_y*0.85)
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Helvetica', 50),
                                     parent = self,
                                     color = 'black',
                                     position = score_label_position)
                                     
        self.start_label = LabelNode(text = 'Tap to start',
                                     font = ('Helvetica', 50),
                                     parent = self,
                                     color = 'black',
                                     position = self.size/2)
                                     
                                     
        highscore_label_position = Vector2(self.size_of_screen_x/2, self.size_of_screen_y/2.4)
        self.highscore_label = LabelNode(text = 'Highscore: ' + str(self.high_score),
                                     font = ('Helvetica', 50),
                                     parent = self,
                                     color = 'black',
                                     position = highscore_label_position,
                                     alpha = 0)
                                     
        #self.fly_bottom = False
        self.current_y_position = self.size_of_screen_y * 0.5
        self.left_or_right = (self.size_of_screen_x * 0.07)*1
        self.left_or_right_left = (self.size_of_screen_x * 0.3)*1
        self.dead = False
        self.menu_button_created = False
        self.score = 0
        self.score_done = False
        self.move_up_speed = 1.5
        self.move_down_speed = 12
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        #print self.score
        if self.score_bottom.frame.contains_rect(self.character.frame) and self.score_done == False:
            self.score = self.score + 1
            sound.play_effect('./assets/Sounds/Coin_4.caf')
            self.score_label.text = 'Score: ' + str(self.score)
            self.score_done = True
        
        if self.character.frame.intersects(self.left_side_border.frame):
            self.score_done = False
            self.left_or_right = (self.size_of_screen_x * 0.07)* -1
            self.left_or_right_left = (self.size_of_screen_x * 0.3)* -1
            
        if self.character.frame.intersects(self.right_side_border.frame):
            self.score_done = False
            self.left_or_right = (self.size_of_screen_x * 0.07)* 1
            self.left_or_right_left = (self.size_of_screen_x * 0.3)* 1
            
        if self.character.frame.intersects(self.bottom_border.frame) or self.character.frame.intersects(self.top_border.frame):
            #sound.play_effect('arcade:Explosion_1')
            self.dead = True
            
        if self.pillar_top.frame.intersects(self.character.frame) or self.pillar_bottom.frame.intersects(self.character.frame):
            #sound.play_effect('arcade:Explosion_1')
            self.dead = True
            
        if self.dead == True:
            #sound.set_volume(0)
            
            self.menu_button.alpha = 1
            self.highscore_label.alpha = 1
            self.character.remove_from_parent()
            self.menu_button_created = True
            high_score_file = open('./high_score.txt', 'r+')
            high_scores = json.load(high_score_file)
            high_scores.append(self.score)
            self.high_score = max(high_scores)
            #print self.high_score
            high_score_file.seek(0)
            json.dump(high_scores, high_score_file)
            high_score_file.close()
            self.highscore_label.text = 'Highscore: ' + str(self.high_score)
            

    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.play_button.frame.contains_point(touch.location) and self.dead == False:
            self.start_label.alpha = 0
            sound.play_effect('./assets/Sounds/Woosh_1.caf')
            self.character.run_action(Action.sequence(Action.move_by(self.left_or_right,100,self.move_up_speed),
                                      Action.move_by(self.left_or_right_left,-2000,self.move_down_speed)))
                                      
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = 0.48
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.menu_button.frame.contains_point(touch.location) and self.dead == True:
            #sound.set_volume(1)
            self.menu_button.scale = 0.5
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
