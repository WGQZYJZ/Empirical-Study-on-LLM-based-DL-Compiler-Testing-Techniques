input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.diagflat(input_tensor, offset=1)