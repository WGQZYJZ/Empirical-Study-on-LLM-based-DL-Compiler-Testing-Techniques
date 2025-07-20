data = torch.arange(0, 100).reshape(10, 10)
indices = torch.tensor([[0, 1, 2, 3], [7, 8, 9, 4]])
result = torch.Tensor.take_along_dim(data, indices, dim=1)