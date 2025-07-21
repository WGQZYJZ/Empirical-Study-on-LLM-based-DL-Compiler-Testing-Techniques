data = torch.randn(2, 3, 5)
pool = torch.nn.LPPool1d(norm_type=2, kernel_size=3, stride=None, ceil_mode=False)
pool_output = pool(data)