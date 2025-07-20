_input_tensor = torch.rand(3, 3, dtype=torch.float32)
_output_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)