input_tensor = torch.randn(3, 4)
result = torch.Tensor.unbind(input_tensor, dim=0)