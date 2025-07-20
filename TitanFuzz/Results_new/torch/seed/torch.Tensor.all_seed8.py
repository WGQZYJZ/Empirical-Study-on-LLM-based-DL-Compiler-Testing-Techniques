input_tensor = torch.randn(2, 3, 3)
output_tensor = torch.Tensor.all(input_tensor, dim=1, keepdim=True)