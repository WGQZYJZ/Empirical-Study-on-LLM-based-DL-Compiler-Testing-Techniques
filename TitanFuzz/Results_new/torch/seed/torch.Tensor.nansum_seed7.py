input_data = torch.randn(4, 4)
result = torch.Tensor.nansum(input_data, dim=0, keepdim=False, dtype=None)