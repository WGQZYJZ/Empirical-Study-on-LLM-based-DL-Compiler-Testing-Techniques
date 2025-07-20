input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_tensor = torch.Tensor.roll(input_tensor, shifts=1, dims=1)