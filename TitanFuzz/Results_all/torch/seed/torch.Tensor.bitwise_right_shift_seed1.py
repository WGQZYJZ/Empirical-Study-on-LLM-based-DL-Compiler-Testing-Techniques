input_tensor = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=torch.int32)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, 2)