input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.aminmax(input_tensor, dim=None, keepdim=False)