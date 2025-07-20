input_tensor = torch.randn(2, 3, 4, 5)
result = torch.Tensor.bool(input_tensor, memory_format=torch.preserve_format)