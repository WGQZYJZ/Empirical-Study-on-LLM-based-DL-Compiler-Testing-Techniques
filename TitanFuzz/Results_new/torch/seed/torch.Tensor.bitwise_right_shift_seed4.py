input_tensor = torch.arange(0, 10, 1, dtype=torch.int32)
right_shift_tensor = torch.Tensor.bitwise_right_shift(input_tensor, 2)