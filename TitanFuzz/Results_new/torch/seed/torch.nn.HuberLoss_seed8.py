input_data = torch.tensor([[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
target_data = torch.tensor([[0.0], [1.0], [1.0], [0.0]])
loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
loss_value = loss(input_data, target_data)