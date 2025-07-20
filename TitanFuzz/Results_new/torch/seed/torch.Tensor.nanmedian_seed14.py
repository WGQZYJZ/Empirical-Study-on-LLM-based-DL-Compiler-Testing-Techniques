input_tensor = torch.randn(3, 4)
input_tensor[(1, 2)] = float('nan')
input_tensor[(2, 3)] = float('nan')
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)