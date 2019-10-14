import rosbag
import os
import numpy as np
import cv2
from cv_bridge import CvBridge

# IMAGE_SIZE = 960 #960 by 960 (array is 921,600 big)

#open bag files
file_input = os.environ['BAGFILE_PATH']
file_output = os.environ['OUTPUT_PATH']
bag_input = rosbag.Bag(file_input)
bag_output = rosbag.Bag(file_output, 'w')
# get topic
my_topics = bag_input.get_type_and_topic_info()[1].keys()
topic_compressedImage = my_topics[0]
#create bridge object
bridge = CvBridge()

#loop over all images
i = 0
for topic, msg, t in bag_input.read_messages(topics=topic_compressedImage):
    timestamp = t.to_time()
    cv_image = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="passthrough")
    text = str(timestamp)
    coord = (50, 50) #(x,y)
    cv2.putText(cv_image, text, coord, cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    new_image = bridge.cv2_to_compressed_imgmsg(cv_image)
    # print(type(msg))
    # print(type(cv_image))
    # print(type(new_image))

    try:
        bag_output.write(topic_compressedImage, new_image, t=t)
    except:
        print("Error: Could not write message to bag file!")
    i+=1
    if i%10==0:
        print('Finished {:d} images...').format(i)

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow( 'image', cv_image)
    # cv2.waitKey(0);
    # cv2.destroyAllWindows()

#close bagfiles
bag_input.close()
bag_output.close()
