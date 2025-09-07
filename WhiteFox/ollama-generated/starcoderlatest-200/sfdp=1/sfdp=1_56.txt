
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.qkv = torch.nn.Linear(embed_dim, embed_dim * 3, bias=False)
 
    def forward(self, q, k, v):
        batch_size = q.shape[0]
        num_heads = self.qkv.weight.shape[0] // self.qkv.in_features
        head_dim = self.qkv.in_features // num_heads

        # Split input tensors into 3 pieces (query, key and value)
        q1, k1, v1 = torch.split(self.qkv(q), num_chunks=num_heads, dim=-2)
        q2, k2, v2 = torch.split(self.qkv(k), num_chunks=num_heads, dim=-2)
        q3, k3, v3 = torch.split(self.qkv(v), num_chunks=num_heads, dim=-2)

        # Apply splitted tensors into 3 heads, and concatenate the result together back to a single tensor with dimension -2 (head_dim * 3)
        q_head, k_head, v_head = torch.cat((q1, q2, q3), dim=-1), torch.cat((k1, k2, k3), dim=-1), torch.cat((v1, v2, v3), dim=-1)

        # Compute the dot product of head tensors
        q_head = q_head.permute(0, 2, 1, 3).contiguous().view(-1, head_dim * 3)
        k_head = k_head.permute(0, 2, 3, 1).contiguous().view(-1, head_dim * 3)
        v_head = v_head.permute(0, 2, 3, 1).contiguous().view(-1, head_dim * 3)

        qk = torch.matmul(q_head, k_head.transpose(-2, -1))

        # Apply scale factor after computing the dot product
        inv_scale_factor = (1.0 / math.sqrt(head_dim)) ** 0.5
        scaled_qk = qk.div(inv_scale_factor)

        # Compute softmax of scaled_qk tensor
        softmax_qk = scaled_qk.softmax(dim=-1)

        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        return torch.matmul(dropout_qk, v_head).contiguous().view(batch_size, embed_dim, -1).permute(0, 2, 1)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = MultiHeadAttention(embed_dim=64)

    def forward(self, x1, x2):
        v1 = self.attn(x1, x1, x1)  # Compute the output of the multi-head attention between x1 and itself (for self-attention)
        v2 = self.attn(x2, x1, v1)  # Compute the output of the multi-head attention between x2 and x1, with self-attention as input to this layer

        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 64, 64)
x2 = torch.randn(32, 64, 64)
