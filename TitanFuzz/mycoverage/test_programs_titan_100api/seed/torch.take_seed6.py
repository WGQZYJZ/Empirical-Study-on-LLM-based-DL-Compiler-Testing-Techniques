input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 1, 2, 0, 1, 2, 0, 1, 2])
output = torch.take(input, index)