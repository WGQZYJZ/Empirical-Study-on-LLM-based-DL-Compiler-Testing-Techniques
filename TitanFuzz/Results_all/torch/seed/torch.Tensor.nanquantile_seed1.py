input_tensor = torch.randn(4, 4)
input_tensor[(1, 1)] = torch.tensor(float('nan'))
input_tensor[(2, 2)] = torch.tensor(float('nan'))
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5)