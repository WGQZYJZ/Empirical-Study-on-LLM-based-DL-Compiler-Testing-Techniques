_input_tensor = torch.randn(2, 3, 3, 3, 3)
_output_tensor = torch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)