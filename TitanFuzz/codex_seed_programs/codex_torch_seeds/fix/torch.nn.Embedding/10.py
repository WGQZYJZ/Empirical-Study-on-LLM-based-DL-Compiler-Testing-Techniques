'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Embedding\ntorch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False, _weight=None, device=None, dtype=None)\n'
import torch
import torch.nn as nn
word_to_ix = {'hello': 0, 'world': 1}
embeds = nn.Embedding(2, 5)
lookup_tensor = torch.tensor([word_to_ix['hello']], dtype=torch.long)
hello_embed = embeds(lookup_tensor)
print(hello_embed)
CONTEXT_SIZE = 2
EMBEDDING_DIM = 10