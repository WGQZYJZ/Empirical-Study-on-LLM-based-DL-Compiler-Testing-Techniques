_input_tensor = torch.rand(2, 3, 4, 5)
_output_tensor = torch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)