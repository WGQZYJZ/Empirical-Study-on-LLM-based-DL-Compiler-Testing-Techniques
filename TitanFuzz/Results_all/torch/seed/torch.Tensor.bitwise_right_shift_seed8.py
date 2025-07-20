input_tensor = torch.randint(low=0, high=128, size=(3, 4), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, other=1)