x = torch.randn(1)
torch.set_rng_state(torch.get_rng_state())
y = torch.randn(1)
if torch.equal(x, y):
    print('Same')
else:
    print('Different')