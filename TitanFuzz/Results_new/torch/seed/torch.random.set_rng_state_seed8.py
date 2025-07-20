input_data = torch.rand(2, 3)
rng_state = torch.get_rng_state()
torch.random.set_rng_state(rng_state)
output_data = torch.rand(2, 3)
if torch.equal(input_data, output_data):
    print('The two random numbers are the same.')
else:
    print('The two random numbers are different.')