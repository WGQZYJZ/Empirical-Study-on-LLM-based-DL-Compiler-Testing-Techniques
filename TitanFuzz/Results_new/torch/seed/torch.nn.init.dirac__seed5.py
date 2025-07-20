input_data = torch.randn(2, 3, 3, 3)
torch.nn.init.dirac_(input_data, groups=1)