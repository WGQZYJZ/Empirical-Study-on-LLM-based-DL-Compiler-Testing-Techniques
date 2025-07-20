input_tensor = torch.randn(2, 3, 4, 5, 6)
result = torch.Tensor.is_contiguous(input_tensor, memory_format=torch.contiguous_format)