input_data = torch.randn((2, 3, 4), dtype=torch.float32)
bool_tensor = torch.Tensor.bool(input_data)
bool_tensor = torch.Tensor.bool(input_data, memory_format=torch.channels_last)