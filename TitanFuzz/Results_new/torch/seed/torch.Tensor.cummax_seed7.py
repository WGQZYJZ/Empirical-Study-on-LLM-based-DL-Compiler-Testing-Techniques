input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.cummax(input_tensor, dim=0)