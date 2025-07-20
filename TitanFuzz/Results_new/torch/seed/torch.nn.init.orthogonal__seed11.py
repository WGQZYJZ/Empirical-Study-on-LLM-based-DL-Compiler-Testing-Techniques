input_size = 2
output_size = 3
input_data = Variable(torch.randn(input_size, output_size))
torch.nn.init.orthogonal_(input_data)