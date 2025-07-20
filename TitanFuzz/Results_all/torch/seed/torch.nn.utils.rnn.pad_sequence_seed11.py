data = [torch.rand(3, 3), torch.rand(4, 3), torch.rand(2, 3)]
padded = torch.nn.utils.rnn.pad_sequence(data)