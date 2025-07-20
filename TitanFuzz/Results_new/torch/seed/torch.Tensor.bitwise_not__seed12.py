input_tensor = torch.tensor([[0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1]], dtype=torch.uint8)
result = torch.Tensor.bitwise_not_(input_tensor)