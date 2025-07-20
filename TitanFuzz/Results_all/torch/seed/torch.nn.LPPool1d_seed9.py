dtype = torch.FloatTensor
input_data = Variable(torch.randn(1, 1, 4).type(dtype))
pool = torch.nn.LPPool1d(norm_type=1, kernel_size=2, stride=2)