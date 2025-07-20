sequences = [torch.tensor([1, 2, 3]), torch.tensor([4, 5]), torch.tensor([6, 7, 8, 9])]
padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences)
padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True)
padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences, padding_value=1)