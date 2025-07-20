if True:
    input = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
    other = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
    print('Input: ', input)
    print('Other: ', other)
    output = torch.bitwise_right_shift(input, other)
    print('Output: ', output)