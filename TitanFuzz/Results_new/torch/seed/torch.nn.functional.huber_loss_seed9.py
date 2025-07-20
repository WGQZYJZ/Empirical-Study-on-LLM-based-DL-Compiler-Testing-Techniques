input = torch.randn(5, requires_grad=True)
target = torch.randn(5)
loss = torch.nn.functional.huber_loss(input, target, delta=1.0)
loss.backward()