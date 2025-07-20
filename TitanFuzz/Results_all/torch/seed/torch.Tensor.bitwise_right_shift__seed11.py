input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=torch.int8)
bitwise_right_shift_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, 1)