data = torch.rand(2, 3)
torch.nn.init.uniform_(data, a=(- 1.0), b=1.0)
data = torch.rand(2, 3)
torch.nn.init.uniform_(data, a=(- 1.0))
data = torch.rand(2, 3)
torch.nn.init.uniform_(data)