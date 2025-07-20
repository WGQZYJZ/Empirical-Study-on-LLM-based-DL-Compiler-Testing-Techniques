input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
swap_tensor = torch.Tensor.swapaxes(input_tensor, 0, 1)