
class MultiHeadAttnModel(torch.nn.Module):
    def __init__(self, h=8, n_attn_heads=4, dim=128):
        super().__init__()
        self.query = torch.nn.Linear(3, dim * h, bias=True)
        self.key   = torch.nn.Linear(3, dim * h, bias=True)
        self.value = torch.nn.Linear(3, dim * h, bias=True)
 
    def forward(self, qk_input):
        bs, n_attn_heads, dim_per_head, seq_len = qk_input.shape
        # [bs x dim * 8 x (n + k) / d]
        query = self.query(qk_input[:, :, :, :])
        key   = self.key(qk_input[:, :, :, n_attn_heads:]).transpose(-2, -1).reshape(bs, n_attn_heads, dim_per_head * 8, (seq_len - n_attn_heads + 1)) # [b x n_heads x d/h x (q.s - n)]
        value = self.value(qk_input[:, :, :, n_attn_heads:]).transpose(-2, -1).reshape(bs, n_attn_heads, dim_per_head * 8, (seq_len - n_attn_heads + 1)) # [b x n_heads x d/h x (q.s - n)]
 
        # [b x n_heads x 8 x (q.s - n)]
        attn_weight = torch.matmul(query, key) # [bs x n_attn_heads x 1 x 1]
        attn_weight = attn_weight / math.sqrt(dim_per_head)  # Scale the dot product by the square root of the value dimension

        # [b x n_attn_heads x 8 x (q.s - n)] + [b x d/h x 1 x seq]
        attn_weight = F.dropout2d(attn_weight, dropout_p=dropout_p) # Dropout
        output = torch.matmul(attn_weight, value) # Compute the dot product of the attention weights and the values
 
        return output


# Initializing the model
m = MultiHeadAttnModel()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
