input_data = torch.randn(5, 5)
rng_state = torch.random.get_rng_state()
torch.random.set_rng_state(rng_state)
rng_state = torch.random.get_rng_state()