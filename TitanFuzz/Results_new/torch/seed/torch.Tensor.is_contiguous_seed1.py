_input_tensor = torch.rand(2, 3, 4)
_result = torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)