input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.index_add_(input_tensor, dim=1, index=index, tensor=tensor)