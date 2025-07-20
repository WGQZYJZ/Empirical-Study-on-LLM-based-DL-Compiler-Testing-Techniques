input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.q_scale(input_tensor)