t = torch.tanh(x)  # tanh activations
p = torch.softmax(x, dim=-1)  # softmax activation (in this example we are not using it)
o = t * p # scaled dot product activation
t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
o1 = t1*0.5 + t1*0.7071067811865476 # Multiply both outputs of the convolution by either 0.5 or 0.7071067811865476
t2 = torch.sigmoid(o1) # Apply sigmoid to the output of the convolution
t3 = t2*0.5 + (1 - t2)*0.7071067811865476 # Multiply both outputs of the convolution by either 0.5 or 0.7071067811865476
t4 = torch.tanh(t3) # Apply tanh to both outputs of the convolution
t5 = t2*1 + (1 - t2)*-0.5 # Multiply both outputs of the convolution by by by f f f f f f s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s
