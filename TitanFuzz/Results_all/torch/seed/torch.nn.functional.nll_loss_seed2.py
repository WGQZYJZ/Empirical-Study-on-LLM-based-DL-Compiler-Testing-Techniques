input_data = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = torch.nn.functional.nll_loss(input_data, target)