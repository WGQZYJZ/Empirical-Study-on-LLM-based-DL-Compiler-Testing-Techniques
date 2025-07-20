input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[True, False, False], [False, True, False], [False, False, True]])
tensor = torch.tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)