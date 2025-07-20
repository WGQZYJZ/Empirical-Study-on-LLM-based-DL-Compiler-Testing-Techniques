input_tensor = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
torch.Tensor.xlogy_(input_tensor, other)