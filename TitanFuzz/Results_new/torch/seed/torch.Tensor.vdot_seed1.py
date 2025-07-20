input_tensor = torch.randn(4, 3)
other_tensor = torch.randn(3, 4)
dot_product = torch.Tensor.vdot(input_tensor, other_tensor)