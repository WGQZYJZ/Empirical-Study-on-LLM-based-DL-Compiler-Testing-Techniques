data = torch.randn((128, 64))
output = torch.nn.BatchNorm1d(64)(data)