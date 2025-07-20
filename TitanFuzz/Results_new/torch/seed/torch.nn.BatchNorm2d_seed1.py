input = torch.randn(20, 5, 35, 45)
batch_norm = torch.nn.BatchNorm2d(5)
output = batch_norm(input)