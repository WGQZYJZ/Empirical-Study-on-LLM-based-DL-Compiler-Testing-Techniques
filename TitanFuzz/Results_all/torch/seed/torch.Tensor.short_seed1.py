_input_tensor = torch.randn(2, 3, 5, 5)
_output_tensor = torch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)