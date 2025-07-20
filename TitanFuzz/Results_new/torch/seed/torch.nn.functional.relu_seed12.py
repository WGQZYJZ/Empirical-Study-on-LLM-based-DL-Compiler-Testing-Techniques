x = torch.randn(3, 4)
y = torch.nn.functional.relu(x)
y = torch.nn.functional.relu(x, inplace=True)