input_tensor = torch.randn(6, 3)
split_size_or_sections = 2
output_tensor = torch.Tensor.vsplit(input_tensor, split_size_or_sections)
split_size_or_sections = [2, 3]
output_tensor = torch.Tensor.vsplit(input_tensor, split_size_or_sections)