input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_tensor = torch.Tensor.narrow_copy(input_tensor, dimension=0, start=1, length=2)