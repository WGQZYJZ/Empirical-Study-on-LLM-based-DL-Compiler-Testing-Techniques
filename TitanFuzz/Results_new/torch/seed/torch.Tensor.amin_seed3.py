input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.amin(input_tensor, dim=1, keepdim=False)