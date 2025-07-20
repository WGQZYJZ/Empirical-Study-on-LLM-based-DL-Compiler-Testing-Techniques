x = torch.empty(3, 3)
torch.nn.init.uniform_(x, a=0.0, b=1.0)
x = torch.empty(3, 3)
torch.nn.init.normal_(x, mean=0.0, std=1.0)