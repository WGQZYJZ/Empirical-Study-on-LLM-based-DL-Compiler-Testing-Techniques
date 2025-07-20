input = torch.randint(low=0, high=10, size=(2, 3, 4))
rot90_input = torch.rot90(input, k=1, dims=(1, 2))
rot180_input = torch.rot90(input, k=2, dims=(1, 2))
rot270_input = torch.rot90(input, k=3, dims=(1, 2))