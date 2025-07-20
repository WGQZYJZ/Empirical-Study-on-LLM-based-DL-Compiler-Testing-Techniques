_input_tensor = torch.rand(1, 2, 3, 4)
_output_tensor = torch.Tensor.bfloat16(_input_tensor, memory_format=torch.preserve_format)