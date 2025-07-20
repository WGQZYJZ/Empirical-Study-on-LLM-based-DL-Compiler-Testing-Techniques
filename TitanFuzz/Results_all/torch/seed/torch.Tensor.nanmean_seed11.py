input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=torch.float)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=0, keepdim=False, dtype=None)