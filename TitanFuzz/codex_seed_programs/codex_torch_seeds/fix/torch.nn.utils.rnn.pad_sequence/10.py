'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
from torch.nn.utils.rnn import pad_sequence
data = [torch.rand(3, 4), torch.rand(4, 4), torch.rand(2, 4), torch.rand(1, 4)]
padded_data = pad_sequence(data, batch_first=False, padding_value=0.0)
print(padded_data)
print(padded_data.shape)