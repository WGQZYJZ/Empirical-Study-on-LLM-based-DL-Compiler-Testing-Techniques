input = Variable(torch.randn(1, 3, 10))
torch.nn.functional.adaptive_avg_pool1d(input, output_size=5)