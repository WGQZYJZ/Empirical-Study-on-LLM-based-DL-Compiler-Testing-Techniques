_input_tensor = torch.rand(3, 3, 3, 3)
result = torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)