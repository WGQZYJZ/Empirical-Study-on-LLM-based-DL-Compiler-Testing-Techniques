input_data = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1]])
other_data = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]])
result = torch.Tensor.bitwise_xor_(input_data, other_data)