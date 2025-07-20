input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)