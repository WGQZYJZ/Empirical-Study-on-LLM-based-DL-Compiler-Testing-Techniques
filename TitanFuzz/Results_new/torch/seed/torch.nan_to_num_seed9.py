x = Variable(torch.FloatTensor([float('nan'), float('inf'), float('-inf'), 0]), requires_grad=True)
y = torch.nan_to_num(x)