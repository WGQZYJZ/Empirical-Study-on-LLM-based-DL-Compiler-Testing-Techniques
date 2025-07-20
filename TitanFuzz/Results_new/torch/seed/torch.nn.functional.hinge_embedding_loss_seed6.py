input = torch.tensor([[(- 0.5), 0.5, 1.5]])
target = torch.tensor([[1, 0, (- 1)]])
loss = torch.nn.functional.hinge_embedding_loss(input, target)
input = torch.tensor([[0.5, 0.5, 0.5]])