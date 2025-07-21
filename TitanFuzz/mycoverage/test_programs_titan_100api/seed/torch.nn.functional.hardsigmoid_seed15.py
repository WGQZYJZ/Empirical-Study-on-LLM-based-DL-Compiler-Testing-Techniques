if True:
    input = torch.randn(1, 3)
    output = torch.nn.functional.hardsigmoid(input)
    print(output)