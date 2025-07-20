input_data = torch.rand(2, 3)
result = torch.jit.isinstance(input_data, torch.Tensor)