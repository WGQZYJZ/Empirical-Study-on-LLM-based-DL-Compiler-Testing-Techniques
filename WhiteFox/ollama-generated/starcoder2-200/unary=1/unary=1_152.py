t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5 # Multiply the output of the convolution by 0.5
t3 = t1 + t1*0.7978845608028654 # Add the output of the convolution to itself multiplied by 0.7978845608028654
t4 = torch.tanh(t3) # Apply hyperbolic tangent function to the output of the convolution
