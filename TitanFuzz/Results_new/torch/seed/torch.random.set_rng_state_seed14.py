x = torch.rand(2, 2)
torch.random.set_rng_state(torch.get_rng_state())
y = torch.rand(2, 2)