input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.diagflat(input_tensor, offset=0)