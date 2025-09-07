
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8, num_layers=1):
        super().__init__()

        self.attn = torch.nn.MultiheadAttention(embed_dim=embed_dim,
                                              num_heads=num_heads)

    def forward(self, qk, attn_mask, dropout_p, value):
        attn_weight = self.attn(qk, qk, qk)[0]

        # The code above is the same as this line (but more concise), but it may cause inconsistency when testing
        # attn_weight = torch.einsum('bijd,bkjds->bidsd', qk, value).transpose(-1, -2)
        # We should also have:
        # qk_t  = query @ key.transpose(-2, -1)
        # output = qk_t * attn_weight.transpose(-2, -1)

        # Attention mask
        attn_weight *= attn_mask

        # Apply softmax and dropout
        attn_weight = torch.softmax(attn_weight, dim=-1)
        output = torch.matmul(attn_weight, value)

        # Dropout the attention weight with probability of dropout_p and add it to the final outputs for training
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        return attn_weight * output + value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 32, 64, 64)
x2 = torch.randn(16, 8, 32, 64)
attn_mask = torch.ones(20, 16).type_as(x1)
dropout_p = 0.5
value = x2


