data = torch.arange(1, 17).view(4, 4)
result = torch.Tensor.tril_(data, diagonal=0)