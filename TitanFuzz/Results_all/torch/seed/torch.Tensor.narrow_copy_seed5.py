input_tensor = torch.rand(5, 3)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 0, 1, 3)