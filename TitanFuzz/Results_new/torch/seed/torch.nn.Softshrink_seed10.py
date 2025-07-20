input_data = torch.randn(10, 10)
softshrink = torch.nn.Softshrink(lambd=0.5)
output = softshrink(input_data)