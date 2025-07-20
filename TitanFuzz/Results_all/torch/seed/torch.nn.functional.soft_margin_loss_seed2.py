input_data = torch.tensor([[1.0, (- 1.0), 1.0], [(- 1.0), 1.0, (- 1.0)], [1.0, (- 1.0), 1.0]])
target_data = torch.tensor([1, (- 1), 1])
loss = torch.nn.functional.soft_margin_loss(input_data, target_data, reduction='sum')