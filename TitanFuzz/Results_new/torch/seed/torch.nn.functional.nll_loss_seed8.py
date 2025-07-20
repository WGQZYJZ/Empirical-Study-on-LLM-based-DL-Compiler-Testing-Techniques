input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = torch.nn.functional.nll_loss(input, target)
loss.backward()
weight = torch.ones(5)
loss = torch.nn.functional.nll_loss(input, target, weight)
loss.backward()
loss = torch.nn.functional.nll_loss(input, target, ignore_index=2)
loss