input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.diag(input_tensor, diagonal=0)
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.diag(input_tensor, diagonal=1)