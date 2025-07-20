input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (4, 3, 4))