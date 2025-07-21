x = torch.randn(3, requires_grad=True)
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())
torch.random.get_rng_state()