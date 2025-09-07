t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5 # Multiply the output of the convolution by 0.5
t3 = t1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
t4 = torch.erf(t3) # Apply the error function to the output of the convolution
t5 = t4 + 1 # Add 1 to the output of the error function
t6 = t2 * t5 # Multiply the output of the convolution by the output of the error function
t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5 # Multiply the output of the convolution by 0.5
t3 = t1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
t4 = torch.erf(t3) # Apply the error function to the output of the convolution
t5 = t4 + 1 # Add 1 to the output of the error function
t6 = t2 * t5 # Multiply the output of the convolution by the output of the error function
t1 = conv(input_tensor) # Apply pointwise convolution with kernel version: ERROR: Error while reading data from ./ ./ Error in /opt/tiny-server/node_modules/pomelo-logger/lib/common.js:209
    at Object.<anonymousanonymousanonymousanonymous anonymous anonymous anonymous anonymous anonymous anonymous anonymous anonymous anonymous anon
