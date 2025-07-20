input = torch.randn(3, requires_grad=True)
torch.set_rng_state(torch.get_rng_state())