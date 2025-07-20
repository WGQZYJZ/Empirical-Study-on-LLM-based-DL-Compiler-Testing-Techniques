input = torch.arange(1, 11)
input = input.view(2, 5)
reps = (2, 3)
output = torch.tile(input, reps)