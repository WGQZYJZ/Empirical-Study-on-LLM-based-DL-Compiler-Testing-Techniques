input_tensor = torch.randn(3, 3)
result = torch.Tensor.cholesky(input_tensor, upper=False)