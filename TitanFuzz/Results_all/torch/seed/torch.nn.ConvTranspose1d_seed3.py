x = torch.randn(1, 1, 4, requires_grad=True)
y = torch.nn.ConvTranspose1d(in_channels=1, out_channels=1, kernel_size=2)
y.forward(x)