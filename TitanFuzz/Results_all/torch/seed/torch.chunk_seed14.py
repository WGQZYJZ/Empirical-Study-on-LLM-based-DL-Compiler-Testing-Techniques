input = torch.randn(8, 3)
output = torch.chunk(input, 3, dim=0)
for i in range(len(output)):
    print('Output[{}]:'.format(i), output[i])