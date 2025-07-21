'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_padded_sequence\ntorch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 0], [6, 0, 0]], dtype=torch.float32)
lengths = torch.tensor([3, 2, 1], dtype=torch.int32)
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input_data, lengths, batch_first=False, enforce_sorted=True)
print(packed_input)
print(packed_input.data)
print(packed_input.batch_sizes)
(padded_input, lengths) = torch.nn.utils.rnn.pad_packed_sequence(packed_input, batch_first=False)
print(padded_input)
print(lengths)