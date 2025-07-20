prediction = torch.rand(10, 1)
target = torch.rand(10, 1)
loss_func = torch.nn.BCELoss()
loss = loss_func(prediction, target)