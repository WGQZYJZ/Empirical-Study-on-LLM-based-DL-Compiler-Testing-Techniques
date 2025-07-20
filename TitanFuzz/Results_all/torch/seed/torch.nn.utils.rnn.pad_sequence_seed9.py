input_data = [torch.randn(3, 3), torch.randn(2, 3), torch.randn(1, 3), torch.randn(1, 3)]
output_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0)