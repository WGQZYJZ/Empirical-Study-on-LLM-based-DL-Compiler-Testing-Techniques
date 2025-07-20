input_tensor = torch.randn(3, 3)
bool_tensor = torch.Tensor.bool(input_tensor, memory_format=torch.preserve_format)