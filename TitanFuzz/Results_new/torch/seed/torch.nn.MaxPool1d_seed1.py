input = torch.randn(20, 16, 50)
max_pool1d = torch.nn.MaxPool1d(3, stride=2)
output = max_pool1d(input)