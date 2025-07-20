input_tensor = torch.randn(2, 3, 4, 1)
output_tensor = torch.Tensor.squeeze(input_tensor, dim=3)