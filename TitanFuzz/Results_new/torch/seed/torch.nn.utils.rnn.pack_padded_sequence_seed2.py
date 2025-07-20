input_data = torch.Tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
lengths = torch.LongTensor([3, 2])
packed_data = torch.nn.utils.rnn.pack_padded_sequence(input_data, lengths, batch_first=True)
padded_data = torch.nn.utils.rnn.pad_packed_sequence(packed_data, batch_first=True)