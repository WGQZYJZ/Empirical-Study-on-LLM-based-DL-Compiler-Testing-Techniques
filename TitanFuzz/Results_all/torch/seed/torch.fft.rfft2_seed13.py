input = Variable(torch.randn(1, 1, 4, 4))
output = torch.fft.rfft2(input, s=None, dim=((- 2), (- 1)), norm=None)