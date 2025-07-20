input_tensor = torch.randn(2, 3, requires_grad=True)
output_tensor = torch.Tensor.arcsinh_(input_tensor)