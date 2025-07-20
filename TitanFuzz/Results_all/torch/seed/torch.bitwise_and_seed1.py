x = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=torch.bool)
y = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.bool)
torch.bitwise_and(x, y)
x = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=torch.bool)