x = torch.randn(5, 5)
y = torch.nn.functional.selu(x)
y = torch.nn.functional.selu(x, inplace=True)
y = torch.nn.functional.selu(x)