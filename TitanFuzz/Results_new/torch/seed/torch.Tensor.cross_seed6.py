input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
result = torch.Tensor.cross(input_tensor, other, dim=(- 1))