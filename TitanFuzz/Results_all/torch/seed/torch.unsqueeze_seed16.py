x = torch.tensor([[1, 2], [3, 4], [5, 6]])
y = torch.unsqueeze(x, dim=0)
x = torch.tensor([[1, 2], [3, 4], [5, 6]])
y = torch.unsqueeze(x, dim=1)
x = torch.tensor([[1, 2], [3, 4], [5, 6]])
y = torch.unsqueeze(x, dim=2)