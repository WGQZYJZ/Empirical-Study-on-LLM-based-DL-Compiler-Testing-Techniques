input_tensor = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.int32)
other = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.int32)
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, other)