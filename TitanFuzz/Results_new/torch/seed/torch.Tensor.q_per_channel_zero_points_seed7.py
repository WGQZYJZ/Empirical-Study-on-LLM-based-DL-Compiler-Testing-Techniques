input_tensor = torch.tensor([[3.0, (- 0.5), 2, 7], [4.0, 5.0, 4.0, 8.0]], requires_grad=True)
output_tensor = torch.Tensor.q_per_channel_zero_points(input_tensor)