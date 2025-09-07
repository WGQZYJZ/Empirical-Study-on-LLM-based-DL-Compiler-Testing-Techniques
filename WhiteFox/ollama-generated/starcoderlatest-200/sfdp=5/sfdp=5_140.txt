
class MultiheadAttention(torch.nn.Module):
    def __init__(self, input_dim, num_attention_heads):
        super().__init__()

        self.qkv = torch.nn.Linear(input_dim, input_dim * 3, bias=False)
        self.dropout = torch.nn.Dropout(0.1)
        self.fc = torch.nn.Linear(input_dim, input_dim)

    def forward(self, x):
        # Compute the query, key, and value
        qkkv = self.qkv(x).chunk(3, dim=-1)  # (batch_size, seq_len, d_model * 3)
        q, k, v = qkkv[0], qkkv[1], qkkv[2]  # (batch_size, seq_len, d_head)

        # Perform multi-head attention
        attn_weights = torch.einsum('bds,bds->bs', q, k) / math.sqrt(q.shape[-1])  # (batch_size, seq_len, seq_len)
        attn_weights += self.dropout()

        # Apply softmax to the attention weights to obtain probabilities of each key word and value word
        attn_weights = torch.softmax(attn_weights, dim=-1)  # (batch_size, seq_len, seq_len)
        attn_weights = torch.dropout(attn_weights, dropout_p, True)  # Apply dropout to the softmax output

        # Compute the context vector and concatenate it with the value vectors of all key words for each attention head
        context_vectors = torch.einsum('bds,bdsv->bsod', attn_weights, v)  # (batch_size, seq_len, d_model)

        # Perform final linear layer
        output = self.fc(context_vectors).unsqueeze(dim=1)  # (batch_size, num_attention_heads, seq_len, d_model)

        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        input_dim = 64 * 64  # Number of dimensions in each input tensor
        self.mha1 = MultiheadAttention(input_dim, num_attention_heads=8)
 
    def forward(self, x1, x2):
        v1 = self.mha1(x1)
 
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
