input_tensor = torch.arange(start=0, end=10, step=1, dtype=torch.float32)
output_tensor = torch.Tensor.floor_divide_(input_tensor, 3)