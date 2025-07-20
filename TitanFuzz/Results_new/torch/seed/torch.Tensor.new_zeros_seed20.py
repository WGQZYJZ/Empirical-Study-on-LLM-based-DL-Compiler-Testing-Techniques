input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.new_zeros(input_tensor, (2, 3), dtype=torch.int64)