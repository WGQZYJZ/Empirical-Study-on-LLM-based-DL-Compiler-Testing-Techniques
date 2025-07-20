input_tensor = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
target_tensor = torch.tensor([[0.0], [1.0], [1.0], [0.0]])
loss_fn = torch.nn.SoftMarginLoss()
loss = loss_fn(input_tensor, target_tensor)