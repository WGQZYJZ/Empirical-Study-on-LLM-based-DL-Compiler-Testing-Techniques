input_data = torch.randint(0, 10, (3, 3), dtype=torch.int32)
torch.random.fork_rng()