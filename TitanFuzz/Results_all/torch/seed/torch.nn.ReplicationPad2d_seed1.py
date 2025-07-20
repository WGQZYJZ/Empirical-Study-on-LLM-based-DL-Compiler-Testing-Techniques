input_data = torch.tensor([[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]])
padding = (1, 1, 1, 1)
output_data = torch.nn.ReplicationPad2d(padding)(input_data)