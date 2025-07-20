input_tensor = torch.randn(2, 3, 4)
split_size_or_sections = 2
output_tensor = torch.Tensor.vsplit(input_tensor, split_size_or_sections)