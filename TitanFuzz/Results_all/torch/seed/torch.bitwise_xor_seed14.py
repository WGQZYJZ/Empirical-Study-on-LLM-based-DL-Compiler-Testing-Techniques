input_data = torch.tensor([[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [0, 0, 0, 0]], dtype=torch.bool)
output = torch.bitwise_xor(input_data, input_data)