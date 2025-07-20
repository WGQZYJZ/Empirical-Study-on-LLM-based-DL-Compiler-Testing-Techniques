input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.uint8)
output_data = torch.bitwise_not(input_data)