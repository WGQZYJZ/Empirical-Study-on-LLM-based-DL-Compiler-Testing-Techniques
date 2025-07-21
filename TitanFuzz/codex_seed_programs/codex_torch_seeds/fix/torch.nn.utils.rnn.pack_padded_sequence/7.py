'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_padded_sequence\ntorch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)\n'
import torch
input = torch.randint(0, 10, (5, 3, 4))
lengths = torch.tensor([3, 2, 1, 1, 1])
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=True)
print(packed_input)