input_tensor = torch.rand(2, 2, 2)
output_tensor = torch.Tensor.q_per_channel_scales(input_tensor)