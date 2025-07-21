'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
import torch
input_data = torch.randint(0, 10, (3, 5, 4))
print(input_data)
padded_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0)
print(padded_data)