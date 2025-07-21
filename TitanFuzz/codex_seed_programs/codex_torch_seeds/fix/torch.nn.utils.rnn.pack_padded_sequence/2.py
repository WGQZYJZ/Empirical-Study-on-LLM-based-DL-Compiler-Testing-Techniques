'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_padded_sequence\ntorch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 0], [6, 0, 0]])
lengths = [3, 2, 1]
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)
print(packed_input)