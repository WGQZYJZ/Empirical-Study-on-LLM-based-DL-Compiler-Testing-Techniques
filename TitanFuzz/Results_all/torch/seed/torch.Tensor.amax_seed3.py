input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.amax(input_tensor, dim=1, keepdim=False)