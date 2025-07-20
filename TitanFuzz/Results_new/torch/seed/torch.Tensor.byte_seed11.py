_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)
_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)