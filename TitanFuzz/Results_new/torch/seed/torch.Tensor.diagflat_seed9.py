input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.diagflat(input_tensor, offset=0)