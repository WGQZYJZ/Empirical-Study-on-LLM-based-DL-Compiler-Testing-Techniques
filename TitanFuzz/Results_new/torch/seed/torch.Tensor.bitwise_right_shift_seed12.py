input_tensor = torch.randint(low=0, high=100, size=(1,), dtype=torch.int32)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, 1)