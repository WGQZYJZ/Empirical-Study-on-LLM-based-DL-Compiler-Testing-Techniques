input = torch.randn(2, 3)
torch.nn.functional.hardsigmoid(input)
input = torch.randn(2, 3)
torch.nn.functional.hardtanh(input, min_val=(- 1.0), max_val=1.0)