input_data = Variable(torch.randn(1, 1, 5, 5))
output = torch.nn.functional.avg_pool2d(input_data, (2, 2), stride=2)