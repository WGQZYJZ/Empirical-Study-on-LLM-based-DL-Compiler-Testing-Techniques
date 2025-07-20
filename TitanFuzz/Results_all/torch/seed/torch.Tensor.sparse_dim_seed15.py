input_tensor = torch.tensor([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])
result = torch.Tensor.sparse_dim(input_tensor)