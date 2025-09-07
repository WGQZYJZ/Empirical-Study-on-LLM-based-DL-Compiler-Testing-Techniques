x_shape, x_zero_point = self.conv2.weight.data.size(), self.conv2.weight.data.zero_()  # Initialize the zero point and shape attributes for conv2 weight parameters
if input1.device.type == "cuda":
    v1 = self.conv2(input1)  # Use cuda device to compute matmul(input, weight)
else:
    v1 = torch.matmul(input1, self.conv2.weight.data)
