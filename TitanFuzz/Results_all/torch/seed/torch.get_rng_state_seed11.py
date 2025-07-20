input = torch.randn(2, 3)
torch.set_rng_state(torch.get_rng_state())
input = torch.randn(2, 3)