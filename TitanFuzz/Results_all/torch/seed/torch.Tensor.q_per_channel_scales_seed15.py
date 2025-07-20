input_tensor = torch.randn(1, 3, 4, 4)
output_tensor = torch.Tensor.q_per_channel_scales(input_tensor)