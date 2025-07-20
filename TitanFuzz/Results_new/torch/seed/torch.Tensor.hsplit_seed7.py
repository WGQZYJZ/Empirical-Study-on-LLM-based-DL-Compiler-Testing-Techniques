input_tensor = torch.rand(2, 4)
split_size_or_sections = 2
output_tensor = torch.Tensor.hsplit(input_tensor, split_size_or_sections)
split_size_or_sections = [2, 2]
output_tensor = torch.Tensor.hsplit(input_tensor, split_size_or_sections)