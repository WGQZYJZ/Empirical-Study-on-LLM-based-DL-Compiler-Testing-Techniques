input = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
target = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
loss = torch.nn.functional.hinge_embedding_loss(input, target, margin=1.0, size_average=None, reduce=None, reduction='mean')