x = torch.tensor([1.0, (- 2.0), 3.0, (- 4.0)])
y = torch.tensor([1.0, (- 2.0), 3.0, (- 4.0)])
huber_loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
loss = huber_loss(x, y)