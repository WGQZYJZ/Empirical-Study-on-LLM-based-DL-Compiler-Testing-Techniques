input_tensor = torch.randn(4, 4)
out = torch.Tensor.cholesky_inverse(input_tensor, upper=False)