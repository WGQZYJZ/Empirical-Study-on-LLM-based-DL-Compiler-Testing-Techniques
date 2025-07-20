x = torch.randn(2, 3)
y = torch.unsqueeze(x, 0)
y = torch.unsqueeze(x, 1)
y = torch.unsqueeze(x, 2)