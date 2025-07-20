input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.diag(input_tensor, diagonal=0)