input = torch.randn(4, requires_grad=True)
target = torch.tensor([1, (- 1), 1, (- 1)])
loss = torch.nn.functional.hinge_embedding_loss(input, target)