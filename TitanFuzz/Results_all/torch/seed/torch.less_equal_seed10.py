input_data = Variable(torch.randn(3, 4))
other_data = Variable(torch.randn(3, 4))
torch.less_equal(input_data, other_data)