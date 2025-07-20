input_data = torch.randint(0, 10, (3, 5, 4))
padded_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0)