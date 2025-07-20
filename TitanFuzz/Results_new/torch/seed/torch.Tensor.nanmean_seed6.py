input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
mean_tensor = torch.Tensor.nanmean(input_tensor, dim=0)