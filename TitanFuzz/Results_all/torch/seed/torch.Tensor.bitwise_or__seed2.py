input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0]], dtype=torch.uint8)
other = torch.tensor([[1, 1, 0], [1, 1, 0]], dtype=torch.uint8)
torch.Tensor.bitwise_or_(input_tensor, other)