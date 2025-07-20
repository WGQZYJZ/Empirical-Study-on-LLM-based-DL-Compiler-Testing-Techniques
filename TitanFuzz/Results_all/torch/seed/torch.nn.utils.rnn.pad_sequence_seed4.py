input_data = [torch.randn(2, 3), torch.randn(3, 3), torch.randn(2, 3), torch.randn(3, 3)]
padded_input_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0)