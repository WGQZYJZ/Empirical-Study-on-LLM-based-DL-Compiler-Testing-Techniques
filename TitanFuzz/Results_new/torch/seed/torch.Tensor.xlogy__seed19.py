input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
torch.Tensor.xlogy_(input_tensor, other)