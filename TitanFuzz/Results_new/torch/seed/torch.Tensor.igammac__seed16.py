_input_tensor = torch.randn(2, 3, dtype=torch.float64)
other = torch.randn(2, 3, dtype=torch.float64)
result = torch.Tensor.igammac_(_input_tensor, other)