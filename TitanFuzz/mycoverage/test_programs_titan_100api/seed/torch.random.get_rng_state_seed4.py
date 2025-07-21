x = torch.rand(3, 4)
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())
torch.rand(3, 4)