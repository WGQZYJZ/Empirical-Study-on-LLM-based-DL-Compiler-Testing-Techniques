input_tensor = torch.tensor([[0, 1, 1], [1, 0, 1], [1, 1, 1]])
other = torch.tensor([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
torch.Tensor.bitwise_and_(input_tensor, other)