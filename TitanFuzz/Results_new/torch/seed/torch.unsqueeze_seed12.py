data = torch.tensor([[1, 2], [3, 4]])
result = torch.unsqueeze(data, dim=0)
result = torch.unsqueeze(data, dim=1)
result = torch.unsqueeze(data, dim=(- 1))