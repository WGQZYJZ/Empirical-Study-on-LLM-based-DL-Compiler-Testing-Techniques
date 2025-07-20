input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]])
output_tensor = torch.Tensor.nanmean(input_tensor, dim=1)