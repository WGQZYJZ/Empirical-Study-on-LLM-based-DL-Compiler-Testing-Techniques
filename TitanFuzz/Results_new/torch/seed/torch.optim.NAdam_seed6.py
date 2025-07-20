X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
Y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])
w = torch.tensor([[0.0]], requires_grad=True)
optimizer = torch.optim.NAdam([w], lr=0.001)
for epoch in range(100):
    y_pred = X.mm(w)
    loss = (y_pred - Y).pow(2).sum()
    print(f'Epoch {(epoch + 1)}/100 | Loss: {loss.item():.4f}')