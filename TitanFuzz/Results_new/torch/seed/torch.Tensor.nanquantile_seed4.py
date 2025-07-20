input_tensor = torch.randn(2, 3, 4)
quantile = torch.Tensor.nanquantile(input_tensor, 0.5, dim=2)