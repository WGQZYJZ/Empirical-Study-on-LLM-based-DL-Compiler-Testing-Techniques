input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 0, 1, 2)