x = torch.randn(1, requires_grad=True)
softmax = torch.nn.LogSoftmax(dim=0)
y = softmax(x)