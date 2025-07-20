in_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
out_tensor = torch.Tensor.bitwise_right_shift(in_tensor, 2)