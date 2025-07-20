input = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
output = torch.nn.functional.softsign(input)