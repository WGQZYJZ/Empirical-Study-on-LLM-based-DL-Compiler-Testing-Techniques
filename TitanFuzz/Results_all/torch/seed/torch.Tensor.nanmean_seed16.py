input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=torch.float32)
output_tensor = torch.Tensor.nanmean(input_tensor)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=0)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=1)