input_tensor = torch.randn(5, 5)
output_tensor = torch.Tensor.sum_to_size(input_tensor, 2, 3)
output_tensor = torch.Tensor.sum_to_size(input_tensor, 2, 3, 2)