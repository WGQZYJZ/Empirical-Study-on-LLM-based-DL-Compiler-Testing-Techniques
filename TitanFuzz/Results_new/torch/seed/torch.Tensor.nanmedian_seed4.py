input_tensor = torch.randn(4, 3)
dim = 1
keepdim = True
output_tensor = torch.Tensor.nanmedian(input_tensor, dim, keepdim)