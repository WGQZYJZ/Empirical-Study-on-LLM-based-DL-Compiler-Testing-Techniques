np.random.seed(1)
input_size = 4
output_size = 3
input_data = np.random.randn(input_size, output_size)
input_data = Variable(torch.Tensor(input_data))
torch.nn.init.xavier_normal_(input_data)