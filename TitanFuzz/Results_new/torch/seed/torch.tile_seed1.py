input = torch.arange(0, 9, dtype=torch.float32)
input = input.view(3, 3)
reps = (2, 2)
output = torch.tile(input, reps)