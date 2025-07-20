input_tensor = torch.rand(2, 3)
other = torch.rand(3, 2)
result = torch.Tensor.vdot(input_tensor, other)