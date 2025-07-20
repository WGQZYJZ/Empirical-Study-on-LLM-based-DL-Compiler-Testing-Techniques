input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.long(input_tensor, memory_format=torch.preserve_format)