if True:
    input = torch.randn(4, 4)
    print(input)
    print(torch.cummax(input, dim=0))
    print(torch.cummax(input, dim=1))