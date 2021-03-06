import appdaemon.appapi as appapi

#
# App to turn lights on and off at sunrise and sunset
#
# Args:
#
# on_scene: scene to activate at sunset
# off_scene: scene to activate at sunrise

class OutsideLights(appapi.AppDaemon):

  def initialize(self):
      
    #  Test    
    #self.run_in(self.sunset_cb, 5)
    #self.run_in(self.sunrise_cb, 10)
    
    # Run at Sunrise  
    self.run_at_sunrise(self.sunrise_cb, 0)
    
    # Run at Sunset
    self.run_at_sunset(self.sunset_cb, 0)
    
  def sunrise_cb(self, kwargs):
    self.log("OutsideLights: Sunrise Triggered")
    self.turn_on(self.args["off_scene"])

  def sunset_cb(self, kwargs):
    self.log("OutsideLights: Sunset Triggered")
    self.turn_on(self.args["on_scene"])
