input_tensor = torch.randn(3, 4)
other = torch.tensor([1, 2, 3, 4])
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, other)