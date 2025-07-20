input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
pad = torch.nn.ReplicationPad1d(2)
output = pad(input)