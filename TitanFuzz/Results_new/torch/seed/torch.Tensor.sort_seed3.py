input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)