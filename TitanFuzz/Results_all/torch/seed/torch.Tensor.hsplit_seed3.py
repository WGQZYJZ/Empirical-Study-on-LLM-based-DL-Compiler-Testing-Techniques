_input_tensor = torch.rand(5, 3)
_split_size_or_sections = 2
_splitted_tensor = torch.Tensor.hsplit(_input_tensor, _split_size_or_sections)
_split_size_or_sections = [2, 1]
_splitted_tensor = torch.Tensor.hsplit(_input_tensor, _split_size_or_sections)
_split_size_or_sections = [1, 2]
_splitted_tensor = torch.Tensor.hsplit(_input_tensor, _split_size_or_sections)
_split_size_or_sections = [(- 1), 1]