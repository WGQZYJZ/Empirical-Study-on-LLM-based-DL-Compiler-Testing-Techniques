x = torch.rand(5, 3)
y = torch.rand(5, 3)
diff = (x - y)
result = torch.isclose(diff, torch.zeros(5, 3))