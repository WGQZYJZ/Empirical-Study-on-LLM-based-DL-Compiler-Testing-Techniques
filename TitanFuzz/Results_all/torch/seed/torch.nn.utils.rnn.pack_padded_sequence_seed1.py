input = torch.tensor([[1, 2, 3], [4, 5, 0], [6, 0, 0]])
lengths = [3, 2, 1]
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)