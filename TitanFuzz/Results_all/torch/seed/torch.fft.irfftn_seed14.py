input = Variable(torch.randn(2, 1, 2, 2), requires_grad=True)
output = torch.fft.irfftn(input)