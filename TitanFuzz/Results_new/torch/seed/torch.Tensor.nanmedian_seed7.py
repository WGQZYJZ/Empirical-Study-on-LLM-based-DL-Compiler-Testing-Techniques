input_tensor = torch.rand(4, 4)
input_tensor[(1, 1)] = float('nan')
input_tensor[(2, 2)] = float('nan')
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)