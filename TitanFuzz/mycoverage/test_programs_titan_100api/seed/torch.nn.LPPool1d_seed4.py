x = Variable(torch.randn(2, 3, 5))
pool = torch.nn.LPPool1d(norm_type=2, kernel_size=2, stride=2)
output = pool(x)