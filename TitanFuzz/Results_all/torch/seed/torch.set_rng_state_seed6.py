x = torch.rand(10)
new_state = torch.get_rng_state()
torch.set_rng_state(new_state)