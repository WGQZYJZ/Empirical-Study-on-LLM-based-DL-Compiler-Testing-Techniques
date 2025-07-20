input_data = torch.randn(1, 1, 4, 4)
padding = (1, 1, 1, 1)
output_data = torch.nn.ReplicationPad2d(padding)(input_data)