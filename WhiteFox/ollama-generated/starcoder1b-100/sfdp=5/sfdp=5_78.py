
class Model(torch.nn.Module):
    def __init__(self, qkv_size=None):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if isinstance(qkv_size, int):
            self.qkv = torch.nn.Linear(qkv_size * 4, qkv_size * 3)
            self.proj = torch.nn.Linear(qkv_size, qkv_size)
        else:
            self.qkv = torch.nn.Linear(qkv_size[0] * 4, qkv_size[1])
            self.proj = torch.nn.Linear(qkv_size[0], qkv_size[1])
 
    def forward(self, x1, k2, v):
        x1 = self.conv1(x1)
        qkv = self.qkv(x1).chunk(3, dim=-1)  # The third dimension corresponds to the input feature dimension of the Transformer

        # Apply attention in the two directions:
        # - query --> key
        k2 = torch.matmul(qkv[0], k2) / math.sqrt(self.attention_head_size * qkv[0].size(-1))  # Scale and shift to match `qk`
        attn = self._self_attn(k2, k2)  # Get the dot product between `q2` and `q2`, with a masking for unmasked locations

        # - query --> value
        v = torch.matmul(v, qkv[1]) / math.sqrt(self.attention_head_size * qkv[0].size(-1))
        attn += self._self_attn(v, v)  # Get the dot product between `q1` and `q2`, with a masking for unmasked locations

        # - value --> query
        v = torch.matmul(v, qkv[0]) / math.sqrt(self.attention_head_size * qkv[0].size(-1))
        attn += self._self_attn(v, v)  # Get the dot product between `q1` and `q2`, with a masking for unmasked locations

        output = torch.matmul(attn, k2) / math.sqrt(self.attention_head_size * qkv[0].size(-1))  # Compute the scaled dot product of the attention weights and query
        output = torch.tanh(output)  # Apply tanh to the output for numerical stability
        return self._mlp(output, x2, k3, v3)
 
    def _self_attn(self, x2, x1):
        qk = x2 @ x1.transpose(-2, -1) / math.sqrt(self.attention_head_size * (x2.size(-1) + x1.size(-1)))  # Scale and shift to match `qk`

        attn_mask = qk.eq(0).unsqueeze(-1)  # Get a mask where elements are `1`, if a corresponding element of the query equals zero
        attn_mask = attn_mask.repeat((1, 1, x2.size(-1), 1))  # Repeat to have `(batch, heads, len_q, len_k)`

        qk = qk + attn_mask  # Add the attention mask to `qk`
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        qk = torch.dropout(qk, dropout_p, True)  # Apply dropout to the output

        x2 = torch.matmul(x2, qk) / math.sqrt(self.attention_head_size * (x2.size(-1) + x1.size(-1)))
        return attn_weight @ x1
 
    def _mlp(self, x2, x3, k4, v4):
        x5 = x2 + x3 + x4 + x5  # Add the result from two previous layer of the Transformer
        x5 = self.proj(x5)  # Apply a linear projection to the output

        return torch.softmax(x5, dim=-1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
k2 = torch.randn(8, 4096)
v = torch.randn(8, 512)
