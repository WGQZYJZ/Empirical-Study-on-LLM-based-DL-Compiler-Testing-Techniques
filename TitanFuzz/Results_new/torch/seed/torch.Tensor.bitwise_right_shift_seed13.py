input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=torch.int32)
other = torch.tensor(2, dtype=torch.int32)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, other)