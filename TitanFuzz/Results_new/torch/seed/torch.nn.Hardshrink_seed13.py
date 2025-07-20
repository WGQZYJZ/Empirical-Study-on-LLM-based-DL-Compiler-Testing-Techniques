input_data = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
torch.nn.Hardshrink(lambd=0.5)
torch.nn.Hardshrink(lambd=0.5)(input_data)