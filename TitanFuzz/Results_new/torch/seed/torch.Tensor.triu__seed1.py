input_tensor = torch.randn(2, 3, dtype=torch.float32)
result = torch.Tensor.triu_(input_tensor, diagonal=0)