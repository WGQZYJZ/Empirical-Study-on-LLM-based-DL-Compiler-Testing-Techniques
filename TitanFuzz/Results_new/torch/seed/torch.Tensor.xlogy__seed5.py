input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.Tensor.xlogy_(input_tensor, other)