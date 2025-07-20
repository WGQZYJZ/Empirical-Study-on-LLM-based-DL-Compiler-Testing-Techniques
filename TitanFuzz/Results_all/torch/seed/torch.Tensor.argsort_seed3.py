input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.argsort(input_tensor, dim=(- 1), descending=False)