input_tensor = torch.randn(3, 3, 3)
output_tensor = torch.Tensor.q_per_channel_axis(input_tensor)