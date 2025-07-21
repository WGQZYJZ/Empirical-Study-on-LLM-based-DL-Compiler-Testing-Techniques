'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Embedding\ntorch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False, _weight=None, device=None, dtype=None)\n'
import torch
input_list = [1, 2, 3]
embedding_layer = torch.nn.Embedding(num_embeddings=5, embedding_dim=4)
output_tensor = embedding_layer(torch.tensor(input_list))
print('Input list: ', input_list)
print('Output tensor: ', output_tensor)