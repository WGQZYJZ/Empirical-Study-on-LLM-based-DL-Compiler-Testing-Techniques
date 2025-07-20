input_data = torch.randn(2, 5)
torch.renorm(input_data, p=2, dim=1, maxnorm=1)