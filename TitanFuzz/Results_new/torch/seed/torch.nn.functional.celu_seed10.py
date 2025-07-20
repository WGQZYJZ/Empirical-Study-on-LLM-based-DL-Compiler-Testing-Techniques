input_data = Variable(torch.randn(1, 2, 3, 4))
torch.nn.functional.celu(input_data, alpha=1.0, inplace=False)
input_data = Variable(torch.randn(1, 2, 3, 4))