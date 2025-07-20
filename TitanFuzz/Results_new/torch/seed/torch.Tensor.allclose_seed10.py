input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
result = torch.Tensor.allclose(input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)