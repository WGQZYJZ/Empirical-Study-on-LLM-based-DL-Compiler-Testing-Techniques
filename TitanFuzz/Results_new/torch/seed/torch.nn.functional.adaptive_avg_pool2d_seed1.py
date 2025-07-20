input = Variable(torch.randn(1, 1, 28, 28))
output = torch.nn.functional.adaptive_avg_pool2d(input, output_size=7)