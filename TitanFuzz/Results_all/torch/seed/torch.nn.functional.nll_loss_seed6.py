input = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
target = torch.tensor([1, 0])
loss = torch.nn.functional.nll_loss(input, target)