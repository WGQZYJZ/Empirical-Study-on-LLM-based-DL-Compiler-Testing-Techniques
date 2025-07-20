input_tensor = torch.rand(2, 3)
input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.diagflat(input_tensor, offset=1)