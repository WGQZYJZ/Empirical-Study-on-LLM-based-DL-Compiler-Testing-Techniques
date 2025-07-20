x = torch.randn(1, requires_grad=True)
y = torch.nn.functional.logsigmoid(x)