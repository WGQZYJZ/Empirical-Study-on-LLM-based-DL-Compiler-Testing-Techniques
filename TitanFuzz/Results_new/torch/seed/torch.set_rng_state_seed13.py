input_data = torch.randn(1, 1)
torch.set_rng_state(torch.get_rng_state())
output_data = torch.randn(1, 1)