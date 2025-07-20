input_tensor = torch.randn(10, 10)
other = torch.randn(10, 10)
torch.Tensor.allclose(input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)