data = [torch.randn(3, 5), torch.randn(2, 5)]
padded = torch.nn.utils.rnn.pad_sequence(data, padding_value=0.0)