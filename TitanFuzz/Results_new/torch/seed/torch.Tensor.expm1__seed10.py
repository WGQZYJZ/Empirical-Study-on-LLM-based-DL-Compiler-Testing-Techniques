input_tensor = torch.randn(3, 3, requires_grad=True)
output_tensor = torch.Tensor.expm1_(input_tensor)