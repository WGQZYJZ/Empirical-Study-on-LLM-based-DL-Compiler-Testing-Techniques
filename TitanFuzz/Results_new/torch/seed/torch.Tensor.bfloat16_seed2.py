input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.bfloat16(input_tensor, memory_format=torch.preserve_format)