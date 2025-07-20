input_tensor = torch.rand(3, 4)
output_tensor = torch.Tensor.argsort(input_tensor, dim=(- 1), descending=False)