input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.q_per_channel_scales(input_tensor)