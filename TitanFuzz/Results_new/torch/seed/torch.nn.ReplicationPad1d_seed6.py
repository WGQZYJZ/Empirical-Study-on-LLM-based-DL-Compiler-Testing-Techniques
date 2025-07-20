input_data = torch.ones(1, 1, 3)
pad = torch.nn.ReplicationPad1d(2)
output = pad(input_data)