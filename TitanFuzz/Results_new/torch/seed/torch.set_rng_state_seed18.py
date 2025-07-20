state = torch.get_rng_state()
x = torch.randn(1)
torch.set_rng_state(state)
y = torch.randn(1)