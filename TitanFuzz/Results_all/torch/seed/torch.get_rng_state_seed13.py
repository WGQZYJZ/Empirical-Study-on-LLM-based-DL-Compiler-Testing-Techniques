data = np.random.rand(2, 3)
torch.get_rng_state()
torch.set_rng_state(torch.get_rng_state())