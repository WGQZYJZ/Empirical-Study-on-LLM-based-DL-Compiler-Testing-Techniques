_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.q_per_channel_scales(_input_tensor)