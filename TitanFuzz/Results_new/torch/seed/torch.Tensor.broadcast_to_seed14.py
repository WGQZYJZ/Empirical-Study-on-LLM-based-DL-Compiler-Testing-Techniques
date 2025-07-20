input_data = torch.arange(1, 5, dtype=torch.float32).reshape(1, 2, 2)
output_data = torch.Tensor.broadcast_to(input_data, (2, 2, 2))