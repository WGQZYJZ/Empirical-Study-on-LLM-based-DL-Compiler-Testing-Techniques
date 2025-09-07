
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, nhead, nhid, dropout):
        super().__init__()

        assert nhead % num_attention_heads == 0

        self.nhead = nhead
        self.attn_fc = torch.nn.Linear(nhid, nhead * (num_attention_heads))
        self.proj = torch.nn.Linear(nhead * num_attention_heads, nhid)
        self.dropout = torch.nn.Dropout(p=dropout)

    def split_last_dim_to_heads(self, x):
        x = x.reshape(-1, num_attention_heads, -1, x.size(-1) // num_attention_heads)
        return x.permute([0, 2, 1, 3])

    def merge_last_dim_from_heads(self, x):
        x = x.permute([0, 2, 1, 3]).reshape(-1, num_attention_heads * (attn_len))
        return x

    def forward(self, query, key, value, attn_mask=None):
        # Convert the shape of input from: [B, Lq, Nqk], [B, Lk, Nkv] -> [B, Lq, Nq, Nkv] and then permute to [B, Lq, Nqk, Nkv]
        query = self.split_last_dim_to_heads(query)
        key = self.split_last_dim_to_heads(key)

        # Compute the attention weights
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_model ** 0.5)
        if attn_mask is not None:
            qk += attn_mask

        # Apply softmax and dropout
        attn_weight = self.dropout(F.softmax(qk, dim=-1))

        # Convert the shape of attention weight from [B, Lq, Nqk, Nkv] -> [B, Lq, Nqk * Nkv] and then permute to [B, Lq, Nqk, Nkv],
        # finally merge back into shape: [B, Lq, Nqk, Nkv]
        attn_out = torch.matmul(attn_weight, value)
        attn_out = self.merge_last_dim_from_heads(attn_out)

        output = self.proj(attn_out)
        return output

class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward, dropout=0.1):
        super().__init__()
        
        # Layer norm on input features of layer for this layer
        self.norm1 = torch.nn.LayerNorm(d_model)

        # MultiHeadAttention of transformer model used to compute the attention weights and output of MultiHeadAttention in a single step
        self.self_attn = MultiHeadAttention(nhead=nhead, nhid=dim_feedforward)
        
        # Feed Forward network layer for this layer
        self.norm2 = torch.nn.LayerNorm(d_model)
        self.linear1 = torch.nn.Linear(dim_feedforward, d_model)
        self.dropout1 = torch.nn.Dropout(p=dropout)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(d_model, dim_feedforward)
        self.dropout2 = torch.nn.Dropout(p=dropout)
        
        # Layer norm on output features of layer for this layer
        self.norm3 = torch.nn.LayerNorm(d_model)

    def forward(self, x):
        