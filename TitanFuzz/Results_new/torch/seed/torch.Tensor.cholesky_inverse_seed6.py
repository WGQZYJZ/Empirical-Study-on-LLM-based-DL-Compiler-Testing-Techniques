input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.cholesky_inverse(input_tensor, upper=False)