x = Variable(torch.randn(1, 3, 5, 5))
y = torch.nn.functional.hardtanh(x)