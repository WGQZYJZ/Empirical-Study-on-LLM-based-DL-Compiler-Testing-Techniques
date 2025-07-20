input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
other = torch.tensor(1, dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, other)