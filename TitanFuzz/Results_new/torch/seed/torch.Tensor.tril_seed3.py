input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.tril(input_tensor, diagonal=0)