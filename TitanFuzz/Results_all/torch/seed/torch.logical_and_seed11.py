input1 = torch.tensor([[1, 1, 1, 1], [0, 0, 0, 0]], dtype=torch.bool)
input2 = torch.tensor([[1, 0, 1, 0], [1, 0, 1, 0]], dtype=torch.bool)
torch.logical_and(input1, input2)
input1 = torch.tensor([[1, 1, 1, 1], [0, 0, 0, 0]], dtype=torch.bool)