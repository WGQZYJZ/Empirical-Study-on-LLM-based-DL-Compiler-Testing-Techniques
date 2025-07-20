input_tensor = torch.randn(5, 7)
input_tensor[(2, 4)] = float('NaN')
input_tensor[(1, 6)] = float('NaN')
result = torch.Tensor.nanquantile(input_tensor, 0.5, dim=None, keepdim=False)