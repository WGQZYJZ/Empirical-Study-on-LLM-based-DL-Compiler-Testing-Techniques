input = torch.randn(1, 3)
output = torch.special.expit(input)
output = torch.sigmoid(input)
output = torch.relu(input)