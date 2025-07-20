x = torch.tensor([1, 2, 3, 5])
y = torch.vander(x, increasing=True)
y = torch.vander(x, 3, increasing=True)