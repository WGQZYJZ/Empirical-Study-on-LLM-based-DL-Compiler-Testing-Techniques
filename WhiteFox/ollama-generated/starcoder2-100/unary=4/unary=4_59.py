t1  = conv_transpose(input_tensor)# Apply pointwise deconvolution with kernel size 3 to the input tensor 
t2  = t1 *0.5 # Multiply the output of the convolution by 0.5
t3  = t1*  0.7071067811865476# Multiply the output of the deconvolution with kernel size 3 by 0.7071067811865476
t4 = torch.erf(t3) # Apply error function to the output of the deconvolution
t5= t4 + 1 # Add 1 to the output of the error function
t6= t2 * t5# Multiply the output of the convolution by the output of the error function
