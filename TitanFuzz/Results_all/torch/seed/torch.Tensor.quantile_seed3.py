input_tensor = torch.randn(1, 2, 3)
output_tensor = torch.Tensor.quantile(input_tensor, q=0.5, dim=None, keepdim=False)