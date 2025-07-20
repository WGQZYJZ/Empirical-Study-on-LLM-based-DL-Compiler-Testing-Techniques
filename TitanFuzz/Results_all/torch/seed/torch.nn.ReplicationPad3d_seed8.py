input_data = Variable(torch.Tensor(1, 1, 4, 4, 4).random_(0, 255))
torch.nn.ReplicationPad3d(padding=2)
pad3d = torch.nn.ReplicationPad3d(padding=2)
out = pad3d(input_data)