input_data = torch.randn(2, 3)
new_state = torch.get_rng_state()
torch.set_rng_state(new_state)
output_data = torch.randn(2, 3)