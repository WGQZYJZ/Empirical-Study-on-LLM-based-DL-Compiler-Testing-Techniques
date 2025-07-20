input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.tril_(input_tensor, diagonal=0)