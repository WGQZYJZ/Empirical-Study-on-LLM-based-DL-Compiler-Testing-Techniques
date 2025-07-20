tensor = torch.rand(2, 2)
torch.nn.init.xavier_normal_(tensor, gain=1.0)