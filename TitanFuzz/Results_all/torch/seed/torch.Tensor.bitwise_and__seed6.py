input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
other = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
torch.Tensor.bitwise_and_(input_tensor, other)