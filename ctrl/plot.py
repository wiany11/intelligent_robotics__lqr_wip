from matplotlib import pyplot as plt


#@plot_rotation_and_transition
#    param:
#        Transition
#            [double]
#        Rotation
#            [double]
#        Time
#            [double]
def plot_rotation_and_transition(Transition, Rotation, Time, title):
    plt.figure(figsize=(16,9))
    
    plt.plot(Time, Transition, label="X")
    plt.plot(Time, Rotation, label=u"\u03B8")
    
    plt.title(title)
    
    #box = plt.subplot(111)
    #[lt.set_position([box.x0, box.y0, box.width*0.8, box_height])]
    plt.legend(loc='center left', bbox_to_anchor=(1.025, 0.5))
    plt.xlabel("time", labelpad=10)
    y_lb = plt.ylabel(u"degree(\u00B0)", labelpad=40)
    y_lb.set_rotation(0)
    
    
    plt.show()