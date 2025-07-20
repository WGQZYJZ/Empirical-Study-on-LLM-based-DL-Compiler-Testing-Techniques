input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.cpu(input_tensor, memory_format=torch.preserve_format)