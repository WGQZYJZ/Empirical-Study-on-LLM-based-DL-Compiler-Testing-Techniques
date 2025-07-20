input_tensor = torch.randn(4, 4)
real_tensor = torch.Tensor.isreal(input_tensor)
input_tensor = (torch.randn(4, 4) + (1j * torch.randn(4, 4)))
real_tensor = torch.Tensor.isreal(input_tensor)