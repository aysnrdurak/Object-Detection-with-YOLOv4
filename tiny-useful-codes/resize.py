import cv2
import glob

c = 1
for name in glob.glob('*.png'):
    image = cv2.imread(name)

    up_width = 640
    up_height = 640
    up_points = (up_width, up_height)
    resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)
    filename= "resized_fruits" + str(c) + ".png"
    c+=1
    cv2.imwrite(filename,resized_up)

    cv2.destroyAllWindows()