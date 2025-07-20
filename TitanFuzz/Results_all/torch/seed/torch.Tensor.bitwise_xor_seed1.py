input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.uint8)
other = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=torch.uint8)
result = torch.Tensor.bitwise_xor(input_tensor, other)