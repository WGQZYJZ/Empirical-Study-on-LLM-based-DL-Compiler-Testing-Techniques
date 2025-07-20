input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 1, 1, 2)