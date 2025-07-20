input_data = torch.tensor([[1, 0, 0, 1], [0, 0, 1, 1]], dtype=torch.int8)
output_data = torch.bitwise_xor(input_data, input_data)