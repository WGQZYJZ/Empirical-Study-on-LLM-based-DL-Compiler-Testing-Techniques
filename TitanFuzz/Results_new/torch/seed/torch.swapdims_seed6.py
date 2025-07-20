if True:
    input = torch.randint(low=0, high=10, size=(2, 3, 4))
    print('Input: \n', input)
    output = torch.swapdims(input, dim0=0, dim1=2)
    print('Output: \n', output)