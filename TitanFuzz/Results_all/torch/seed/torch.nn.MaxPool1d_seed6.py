input = torch.randn(20, 16, 50)
m = torch.nn.MaxPool1d(3, stride=2)
output = m(input)