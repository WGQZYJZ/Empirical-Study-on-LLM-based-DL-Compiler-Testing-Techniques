input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_tensor = torch.Tensor.chunk(input_tensor, chunks=2, dim=0)