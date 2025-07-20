if True:
    input_data = torch.randn(3, 4)
    print(input_data)
    print(torch.nonzero(input_data))
    print(torch.nonzero(input_data, as_tuple=True))