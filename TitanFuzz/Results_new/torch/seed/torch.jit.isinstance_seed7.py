input_data = torch.randn(5, 3)
result = torch.jit.isinstance(input_data, torch.Tensor)