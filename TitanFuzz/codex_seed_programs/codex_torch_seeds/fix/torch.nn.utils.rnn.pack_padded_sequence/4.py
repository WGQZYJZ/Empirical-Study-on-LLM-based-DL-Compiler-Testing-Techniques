'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_padded_sequence\ntorch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)\n'
import torch
import torch.nn as nn
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lengths = [3, 2, 1]
packed_input = nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)
print(packed_input)
print(packed_input.data)
print(packed_input.batch_sizes)