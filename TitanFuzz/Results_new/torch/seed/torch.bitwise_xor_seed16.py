input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.int32)
other_tensor = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.int32)
result = torch.bitwise_xor(input_tensor, other_tensor)