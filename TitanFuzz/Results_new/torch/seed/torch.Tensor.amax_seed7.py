input_tensor = torch.randn(3, 5)
output_tensor = torch.Tensor.amax(input_tensor, dim=1, keepdim=True)