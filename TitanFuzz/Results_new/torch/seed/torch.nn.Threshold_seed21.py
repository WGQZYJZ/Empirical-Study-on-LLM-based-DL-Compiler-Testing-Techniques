x = torch.randn(3, 3)
threshold = torch.nn.Threshold(0.5, 0.5)
y = threshold(x)