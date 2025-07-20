input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
exponent = torch.tensor(2, dtype=torch.float32)
output_tensor = torch.Tensor.float_power(input_tensor, exponent)