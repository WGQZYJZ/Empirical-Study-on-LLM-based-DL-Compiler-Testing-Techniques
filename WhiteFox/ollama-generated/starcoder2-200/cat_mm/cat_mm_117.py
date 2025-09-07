t1 = input1  *  5 + 0.2839754086187594 *  (input1  *  input1)
t2 = torch.relu(t1)  # Relu operation is applied to the output of the convolution
