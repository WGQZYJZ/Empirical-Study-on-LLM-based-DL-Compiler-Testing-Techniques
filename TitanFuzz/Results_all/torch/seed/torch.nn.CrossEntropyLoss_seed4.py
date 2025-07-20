y_pred = torch.tensor([[0.1, 0.2, 0.7], [0.3, 0.3, 0.4], [0.7, 0.2, 0.1]])
y_true = torch.tensor([2, 1, 0])
loss = torch.nn.CrossEntropyLoss()