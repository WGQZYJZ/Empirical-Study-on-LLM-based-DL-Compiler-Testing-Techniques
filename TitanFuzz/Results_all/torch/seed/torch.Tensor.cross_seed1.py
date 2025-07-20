input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.Tensor.cross(input_tensor, other, dim=(- 1))