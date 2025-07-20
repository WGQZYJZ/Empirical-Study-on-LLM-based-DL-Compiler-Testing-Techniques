input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int8)
other = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_and_(input_tensor, other)