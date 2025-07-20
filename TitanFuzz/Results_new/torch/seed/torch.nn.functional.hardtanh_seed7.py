x = torch.randn(4, 3)
x_hat = torch.nn.functional.hardtanh(x, min_val=(- 1.0), max_val=1.0, inplace=False)