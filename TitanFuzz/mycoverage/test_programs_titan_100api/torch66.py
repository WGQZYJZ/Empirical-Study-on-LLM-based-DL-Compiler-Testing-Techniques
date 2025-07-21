import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 1], [1, 2]])
output = torch.gather(input, dim=1, index=index)