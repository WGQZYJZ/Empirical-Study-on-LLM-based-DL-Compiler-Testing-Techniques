input = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
input = input.view(1, 1, 10)
pad = (1, 2, 3, 4)
output = torch.nn.functional.pad(input, pad, mode='constant', value=0)