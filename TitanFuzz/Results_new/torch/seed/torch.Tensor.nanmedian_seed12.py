input_tensor = torch.randn(3, 3)
input_tensor[(0, 0)] = float('nan')
median_tensor = torch.Tensor.nanmedian(input_tensor)