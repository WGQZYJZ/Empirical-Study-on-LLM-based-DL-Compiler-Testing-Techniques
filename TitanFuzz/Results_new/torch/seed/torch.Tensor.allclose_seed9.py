_input_tensor = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
_output_tensor = torch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)