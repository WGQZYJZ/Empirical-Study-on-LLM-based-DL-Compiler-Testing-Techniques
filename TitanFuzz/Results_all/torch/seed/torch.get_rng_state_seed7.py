input_data = torch.rand(10)
random_state = torch.get_rng_state()
torch.set_rng_state(random_state)