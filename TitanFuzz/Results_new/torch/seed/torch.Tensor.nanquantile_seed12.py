input_tensor = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]])
result_tensor = torch.Tensor.nanquantile(input_tensor, 0.5)