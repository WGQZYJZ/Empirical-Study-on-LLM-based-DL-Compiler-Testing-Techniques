input_tensor = torch.rand(5, 7)
output_tensor = torch.Tensor.tensor_split(input_tensor, 3, dim=1)