input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
left_shift_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, 2)