input_tensor = torch.rand(1, 3, 4, 4, dtype=torch.float32)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)