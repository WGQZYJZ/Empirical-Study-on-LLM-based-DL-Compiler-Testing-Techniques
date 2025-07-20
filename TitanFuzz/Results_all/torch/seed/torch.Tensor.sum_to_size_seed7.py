input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.sum_to_size(input_tensor, 2, 3)