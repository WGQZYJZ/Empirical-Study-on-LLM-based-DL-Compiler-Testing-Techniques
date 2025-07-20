x = torch.tensor(data=[2.0, 3.0], requires_grad=True)
optimizer = torch.optim.RMSprop([x], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
optimizer.step()