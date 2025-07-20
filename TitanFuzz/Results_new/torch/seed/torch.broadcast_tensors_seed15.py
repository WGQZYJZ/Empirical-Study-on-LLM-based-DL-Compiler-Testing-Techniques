a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
res = torch.broadcast_tensors(a, b)