input_data = torch.randn(2, 3)
output_data = torch.broadcast_tensors(input_data, input_data)