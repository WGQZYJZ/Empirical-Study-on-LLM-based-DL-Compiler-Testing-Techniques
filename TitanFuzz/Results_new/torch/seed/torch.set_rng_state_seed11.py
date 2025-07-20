x = torch.randn(3, 3)
y = torch.randn(3, 3)
new_state = torch.get_rng_state()
torch.set_rng_state(new_state)