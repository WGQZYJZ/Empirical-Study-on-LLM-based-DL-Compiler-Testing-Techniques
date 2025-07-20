input_data = Variable(torch.randn(1, 10))
softshrink_data = torch.nn.functional.softshrink(input_data, lambd=0.5)