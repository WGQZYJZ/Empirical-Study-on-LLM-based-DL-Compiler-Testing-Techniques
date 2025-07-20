input_tensor = torch.arange(1, 17).view(4, 4)
output_tensor = torch.Tensor.diag(input_tensor, diagonal=0)
output_tensor = torch.Tensor.diag(input_tensor, diagonal=(- 1))
output_tensor = torch.Tensor.diag(input_tensor, diagonal=1)