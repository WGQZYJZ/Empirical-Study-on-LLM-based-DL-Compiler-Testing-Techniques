input_data = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.int32)
output_data = torch.bitwise_xor(input_data, input_data)