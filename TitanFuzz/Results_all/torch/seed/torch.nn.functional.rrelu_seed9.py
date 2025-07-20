x = torch.linspace((- 1), 1, 10, requires_grad=True)
y = torch.nn.functional.rrelu(x, lower=0.1, upper=0.2)
y.backward(torch.ones_like(x))