a = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
b = torch.Tensor.bitwise_left_shift(a, 1)