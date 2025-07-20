input_tensor = torch.randn(1, 3, 2, 2)
output_tensor = torch.Tensor.squeeze(input_tensor, dim=0)