x = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
prelu = torch.nn.PReLU()
y = prelu(x)