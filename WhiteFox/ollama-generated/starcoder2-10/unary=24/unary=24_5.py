t2 = torch.nn.ReLU()
t0 = t1 * negative_slope
t1 = torch.where(t3, t0, t4)  # Apply the where function to select elements from the output of the convolution or the result of the multiplication based on the mask
