input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 1, 2], [1, 2, 0]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)