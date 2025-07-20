_input_tensor = torch.randn(4, 4, dtype=torch.float32)
_out_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)