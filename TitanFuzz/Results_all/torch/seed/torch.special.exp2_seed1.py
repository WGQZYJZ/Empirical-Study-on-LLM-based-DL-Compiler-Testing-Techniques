if True:
    a = torch.rand(2, 3, requires_grad=True)
    print(a)
    print(torch.special.exp2(a))