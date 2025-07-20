input_tensor = torch.randn(2, 3, 3)
torch.nn.init.dirac_(input_tensor, groups=1)