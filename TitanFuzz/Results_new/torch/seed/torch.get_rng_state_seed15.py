x = torch.randn(1, requires_grad=True)
torch.get_rng_state()
x = torch.randn(1, requires_grad=True)
torch.set_rng_state(torch.get_rng_state())