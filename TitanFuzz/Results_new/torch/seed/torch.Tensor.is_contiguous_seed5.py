_input_tensor = torch.rand(3, 3)
_is_contiguous = torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)