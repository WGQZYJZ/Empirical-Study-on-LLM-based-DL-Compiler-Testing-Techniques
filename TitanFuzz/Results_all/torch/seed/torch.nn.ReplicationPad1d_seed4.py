input_data = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6]]]))
replication_pad1d = torch.nn.ReplicationPad1d(padding=2)
output = replication_pad1d(input_data)