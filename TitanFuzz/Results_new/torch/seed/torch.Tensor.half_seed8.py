_input_tensor = torch.rand(1000, 1000)
_output_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)
_output_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.channels_last)
_output_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.contiguous_format)
_output_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)