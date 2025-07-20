input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.select(input_tensor, 1, 2)