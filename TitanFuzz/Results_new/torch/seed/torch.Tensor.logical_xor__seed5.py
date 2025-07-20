input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.bool)
other = torch.tensor([[0, 1], [1, 0], [0, 1], [1, 0]], dtype=torch.bool)
torch.Tensor.logical_xor_(input_tensor, other)