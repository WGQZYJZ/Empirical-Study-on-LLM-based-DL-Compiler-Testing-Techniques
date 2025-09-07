t1 = Conv2d(256, 728, kernel_size=(7, 7), stride=(2, 2))
t3 = t1 * 0.9 # Multiply the output by a constant value of 0.9
t4 = torch.tanh(t3) + 0.3 # Add to the previous output a constant value of 0.3
