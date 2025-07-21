'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
input_data = [torch.randn(1, 3), torch.randn(2, 3), torch.randn(3, 3)]
output_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=True)
print(output_data)
print(output_data.shape)