input_tensor = torch.arange(1, 11, dtype=torch.float32).reshape(2, 5)
output_tensor = torch.Tensor.exp_(input_tensor)