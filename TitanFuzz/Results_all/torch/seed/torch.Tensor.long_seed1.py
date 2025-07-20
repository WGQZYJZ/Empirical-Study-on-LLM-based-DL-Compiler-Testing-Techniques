_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.long(_input_tensor)
_output_tensor = torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)