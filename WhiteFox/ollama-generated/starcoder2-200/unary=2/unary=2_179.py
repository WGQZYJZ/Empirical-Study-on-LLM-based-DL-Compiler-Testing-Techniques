t1  = conv(input_tensor)  # Apply pointwise convolution to the input tensor.
t2 = convtranspose(input_tensor)#Apply pointwise transposed convolution to the input tensor
t3 = t2 * -0.549768585395813#Multiply the output of the transposed convolution by a negative constant  −0.549768585395813, the same constant used in the previous model
t4 = t2 * -0.195090322065689#Multiply the output of the transposed convolution by a negative constant  −0.195090322065689, the same constant used in the previous model
t5 = t1 + t4#Add the output of the convolution to the output of the multiplication
t6 = t1 * -0.73543965730667 #Multiply the output of the transposed convolution by a negative constant  −0.73543965730667, the same constant used in the previous model
t7 = t1 + t6#Add the output of the convolution to the output of the multiplication
