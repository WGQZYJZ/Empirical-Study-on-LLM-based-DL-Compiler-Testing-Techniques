x = torch.randn(2, 5)
softmax = torch.nn.Softmax(dim=1)
y = softmax(x)