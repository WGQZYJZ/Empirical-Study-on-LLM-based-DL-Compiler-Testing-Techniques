input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other = torch.tensor([[1, 1], [1, 1]], dtype=torch.float32)
torch.Tensor.sub_(input_tensor, other, alpha=1)