'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiheadAttention\ntorch.nn.MultiheadAttention(embed_dim, num_heads, dropout=0.0, bias=True, add_bias_kv=False, add_zero_attn=False, kdim=None, vdim=None, batch_first=False, device=None, dtype=None)\n'
import torch
input_data = torch.randn(2, 3, 10)
input_data_2 = torch.randn(2, 3, 10)
attn = torch.nn.MultiheadAttention(embed_dim=10, num_heads=2)
(output, attn_weights) = attn.forward(input_data, input_data_2, input_data_2)
print(output)
print(attn_weights)