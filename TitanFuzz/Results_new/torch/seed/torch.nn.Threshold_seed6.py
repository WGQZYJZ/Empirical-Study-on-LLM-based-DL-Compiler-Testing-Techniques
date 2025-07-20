x = torch.rand(2, 3)
threshold = 0.5
value = (- 1)
y = torch.nn.Threshold(threshold, value)(x)
threshold = 0.5
value = (- 1)
y = torch.nn.Threshold(threshold, value, inplace=True)(x)