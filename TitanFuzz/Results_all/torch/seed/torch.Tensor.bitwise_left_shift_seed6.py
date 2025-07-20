input_tensor = torch.rand(2, 3)
other = torch.randint(0, 10, (2, 3))
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, other)