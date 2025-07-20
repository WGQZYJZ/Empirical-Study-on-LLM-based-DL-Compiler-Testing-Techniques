input = torch.randn(1, 1, 5, 5)
torch.nn.functional.rrelu_(input)
torch.nn.functional.rrelu_(input, training=True)
torch.nn.functional.rrelu_(input, lower=0.4, upper=0.6)