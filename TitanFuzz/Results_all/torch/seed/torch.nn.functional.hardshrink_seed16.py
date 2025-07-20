input_data = torch.randn(1, 3, 4, 4)
shrinked_data = torch.nn.functional.hardshrink(input_data, lambd=0.5)