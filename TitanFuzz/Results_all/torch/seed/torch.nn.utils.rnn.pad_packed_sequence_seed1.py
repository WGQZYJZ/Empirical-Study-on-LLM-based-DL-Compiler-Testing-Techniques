input_data = torch.randint(0, 10, (3, 5))
packed_sequence = torch.nn.utils.rnn.pack_padded_sequence(input_data, [5, 3, 2], batch_first=True)
pad_packed_sequence = torch.nn.utils.rnn.pad_packed_sequence(packed_sequence, batch_first=True)