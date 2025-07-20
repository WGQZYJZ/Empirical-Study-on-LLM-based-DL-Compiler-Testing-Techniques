input_data = torch.randn(1, 3, 3, 3)
torch.nn.init.dirac_(input_data, groups=1)