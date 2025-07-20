input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.moveaxis(input_tensor, 0, 2)