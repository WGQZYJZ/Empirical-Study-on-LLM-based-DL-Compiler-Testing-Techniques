tensor = torch.randn(4, 4)
torch.nn.init.normal_(tensor, mean=0.0, std=1.0)