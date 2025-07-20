x = torch.empty(2, 3)
torch.nn.init.normal_(x)
torch.nn.init.normal_(x, mean=0.5, std=0.1)