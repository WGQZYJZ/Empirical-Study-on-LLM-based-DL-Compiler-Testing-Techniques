x = torch.arange((- 10), 10, 0.1)
y = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0, inplace=False)(x)