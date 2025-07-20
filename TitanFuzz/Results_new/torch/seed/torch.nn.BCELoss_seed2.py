y_pred = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
y_true = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
loss_func = torch.nn.BCELoss()
loss = loss_func(y_pred, y_true)