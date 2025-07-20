data = torch.rand(2, 3)
rng_state = torch.get_rng_state()
torch.random.set_rng_state(rng_state)
data = torch.rand(2, 3)