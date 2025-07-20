_input_tensor = torch.rand(size=(4, 4))
_output_tensor = torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)