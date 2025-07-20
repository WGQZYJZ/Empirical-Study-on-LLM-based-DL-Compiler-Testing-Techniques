input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = torch.Tensor.isclose(input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)