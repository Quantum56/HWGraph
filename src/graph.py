import path
from matplotlib.pyplot import figure, legend, plot, show, title, ylim
import os

def graph_create(pointlist, type):

    ##tests with logger
    #logger = logging.getLogger('HWGraph')
    #hdlr = logging.FileHandler('/HWGraph.log')
    #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #hdlr.setFormatter(formatter)
    #logger.addHandler(hdlr) 
    #logger.setLevel(logging.WARNING)

    if path.exists('foo.png'):
        os.remove("foo.png")

    #for x in range(len(pointlist)):
    #    logger.info(str(pointlist[x]))

    figure(1, figsize=(12, 6))

    ylim(top=1)
    plot(pointlist)
    title('Frequency of %s' %type, bbox={'facecolor': '0.8', 'pad': 5})
    legend()
    

    show()  # Actually, don't show, just save to foo.png
    #savefig('foo.png', bbox_inches='tight').