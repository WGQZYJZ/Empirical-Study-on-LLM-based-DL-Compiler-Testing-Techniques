t1  = conv1(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2  = t1 + conv2(conv3(conv4(conv5(conv6(conv7(conv8(conv9(conv10(conv11(conv12(conv13(input_tensor)))))))))))))  # Apply a 1x1 convolution to the output of another pointwise convolution that is applied multiple times
