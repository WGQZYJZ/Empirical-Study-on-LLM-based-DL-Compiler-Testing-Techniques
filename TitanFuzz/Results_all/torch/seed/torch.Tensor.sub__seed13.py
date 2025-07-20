input_tensor = torch.randn(1, 2, 3)
other = torch.randn(1, 2, 3)
torch.Tensor.sub_(input_tensor, other)