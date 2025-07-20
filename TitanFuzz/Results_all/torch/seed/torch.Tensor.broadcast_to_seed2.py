input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (3, 3))