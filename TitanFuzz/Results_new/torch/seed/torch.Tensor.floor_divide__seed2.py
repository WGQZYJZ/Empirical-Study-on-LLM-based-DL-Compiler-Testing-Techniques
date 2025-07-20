input_tensor = torch.arange(1, 11, dtype=torch.float32)
output_tensor = torch.Tensor.floor_divide_(input_tensor, 5)