_input_tensor = torch.randint(0, 255, (1, 3, 3, 3), dtype=torch.uint8)
_output_tensor = torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)