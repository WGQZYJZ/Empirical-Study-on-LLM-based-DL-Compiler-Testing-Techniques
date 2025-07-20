data = torch.randn(1, 1, 4)
pool = torch.nn.AdaptiveAvgPool1d(output_size=2)
pool = torch.nn.AdaptiveAvgPool1d(output_size=1)
pool = torch.nn.AdaptiveAvgPool1d(output_size=3)