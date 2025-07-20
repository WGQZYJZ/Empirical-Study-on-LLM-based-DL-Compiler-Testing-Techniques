x = Variable(torch.randn(1, 1, 5))
pool = torch.nn.functional.adaptive_max_pool1d(x, output_size=3)