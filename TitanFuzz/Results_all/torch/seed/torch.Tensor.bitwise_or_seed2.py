input_tensor = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=torch.int8)
other = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_or(input_tensor, other)