input_tensor = torch.randn((1, 2, 3))
other_tensor = torch.randn((1, 2, 3))
torch.Tensor.xlogy_(input_tensor, other_tensor)