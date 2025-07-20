input_tensor = torch.randn(2, 2)
output_tensor = torch.Tensor.cholesky_inverse(input_tensor, upper=False)