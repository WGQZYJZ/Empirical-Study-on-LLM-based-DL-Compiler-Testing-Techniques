input_data = torch.randn(3, 3)
softshrink = torch.nn.Softshrink(lambd=0.5)
output = softshrink(input_data)