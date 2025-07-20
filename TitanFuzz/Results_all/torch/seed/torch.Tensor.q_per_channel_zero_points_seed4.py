input_data = torch.randn(2, 3, 4)
output_data = torch.Tensor.q_per_channel_zero_points(input_data)