tensor_a = torch.tensor([[4, 4], [8, 8]], dtype=torch.int32)
tensor_b = torch.tensor([[2, 2], [2, 2]], dtype=torch.int32)
tensor_c = torch.bitwise_right_shift(tensor_a, tensor_b)