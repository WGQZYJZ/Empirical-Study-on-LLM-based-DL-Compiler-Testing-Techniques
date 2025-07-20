input_data = torch.randn(1, 1, 3, requires_grad=True)
torch.nn.LazyConvTranspose1d(1, 3, 1, 0, 0, 1, True, 1, 'zeros', None, None)(input_data)