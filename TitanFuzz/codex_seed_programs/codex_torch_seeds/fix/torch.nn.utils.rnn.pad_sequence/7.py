'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
input_data = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3), torch.randn(1, 3)]
print(torch.nn.utils.rnn.pad_sequence(input_data, batch_first=True, padding_value=0.0))
print(torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0))