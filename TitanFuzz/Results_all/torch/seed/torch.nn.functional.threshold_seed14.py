input = Variable(torch.randn(1, 3, 4, 4))
output = torch.nn.functional.threshold(input, threshold=0.5, value=0.0)