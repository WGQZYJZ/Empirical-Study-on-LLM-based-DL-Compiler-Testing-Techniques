input_data = torch.arange(1, 7, dtype=torch.float32).view(1, 1, 6)
padding = 3
output = torch.nn.ReplicationPad1d(padding)(input_data)