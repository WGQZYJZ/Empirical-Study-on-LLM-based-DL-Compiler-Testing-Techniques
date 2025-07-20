x = torch.randn(1, 3, 3, 3)
relu = torch.nn.Hardtanh()
y = relu(x)