input_tensor = torch.randn(4, 4)
result = torch.Tensor.divide_(input_tensor, 2)
result = torch.divide(input_tensor, 2)