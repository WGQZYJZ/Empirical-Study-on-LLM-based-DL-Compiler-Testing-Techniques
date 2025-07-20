input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=0, keepdim=False, dtype=None)