input_tensor = torch.randn(3, 3, requires_grad=True)
output_tensor = torch.Tensor.neg_(input_tensor)