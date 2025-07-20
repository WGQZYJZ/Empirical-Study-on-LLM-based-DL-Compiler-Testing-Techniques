input_tensor = torch.randn(2, 3, 5, 5)
torch.nn.init.dirac_(input_tensor, groups=1)
input_tensor = torch.randn(2, 3, 5, 5)
torch.nn.init.dirac_(input_tensor, groups=1)