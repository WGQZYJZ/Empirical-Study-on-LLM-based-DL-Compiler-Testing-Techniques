input_tensor = torch.rand((3, 3))
other = torch.rand((3, 3))
torch.Tensor.xlogy_(input_tensor, other)