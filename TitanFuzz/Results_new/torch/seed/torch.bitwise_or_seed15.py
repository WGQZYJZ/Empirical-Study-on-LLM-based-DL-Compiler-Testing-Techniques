tensor_a = torch.randint(0, 2, (3, 3), dtype=torch.bool)
tensor_b = torch.randint(0, 2, (3, 3), dtype=torch.bool)
tensor_c = torch.bitwise_or(tensor_a, tensor_b)