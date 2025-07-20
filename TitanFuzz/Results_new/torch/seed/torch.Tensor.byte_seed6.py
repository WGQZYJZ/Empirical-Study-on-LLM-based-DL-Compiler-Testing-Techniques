_input_tensor = torch.randn(3, 3, 3)
_output_tensor = torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)