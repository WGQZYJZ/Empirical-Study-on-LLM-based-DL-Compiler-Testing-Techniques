input_data = torch.randn(3, 5)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = torch.nn.AdaptiveLogSoftmaxWithLoss(5, 5, [3, 4])
output = loss(input_data, target)