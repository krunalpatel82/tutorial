cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",5,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",125,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",105,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)