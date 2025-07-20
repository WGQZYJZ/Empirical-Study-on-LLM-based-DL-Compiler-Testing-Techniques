input_data = [torch.tensor([1, 2, 3]), torch.tensor([4, 5]), torch.tensor([6, 7, 8, 9])]
padded_input = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0)