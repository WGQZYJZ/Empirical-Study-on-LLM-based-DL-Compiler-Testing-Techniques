input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0], [0, 1, 0]], dtype=torch.int8)
result = torch.Tensor.bitwise_not_(input_tensor)