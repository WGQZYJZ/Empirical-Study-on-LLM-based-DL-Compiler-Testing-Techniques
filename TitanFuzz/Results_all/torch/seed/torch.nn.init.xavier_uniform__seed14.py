input_data = Variable(torch.Tensor(2, 3))
torch.nn.init.xavier_uniform_(input_data)