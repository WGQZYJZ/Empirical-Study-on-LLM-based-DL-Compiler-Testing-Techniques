
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_linear = nn.Linear(784, 512)
        self.k_linear = nn.Linear(784, 512)
        self.v_linear = nn.Linear(784, 512)

    def forward(self, x1):
        batch_size = x1.shape[0]
        n_heads = 4
        head_dim = 512
        
        q  = self.q_linear(x1).view(batch_size * n_heads, -1, head_dim)
        k  = self.k_linear(x1).view(batch_size * n_heads, -1, head_dim)
        v  = self.v_linear(x1).view(batch_size * n_heads, -1, head_dim)
        qk  = q @ k.transpose(-2, -1) / math.sqrt(head_dim)
        
        # The softmax function computes the probability of each output of a linear transformation from the last hidden unit to itself. 
        # Therefore we need to add an attention mask which zeros out the probability of the zero-valued entries in the input and adds ones for nonzero values
        attn_mask = torch.zeros(qk.shape[:-1], dtype=x1.dtype, device=x1.device).bernoulli_(attn_p)  # We set a value in the diagonal to zero so that the entry at the position of [i, i] is always 0
        qk = qk + attn_mask  # Add the attention mask
        attn_weight = nn.Softmax(dim=-1)(qk)
        
        # Apply dropout
        output = attn_weight @ v  # Compute dot product (attention weights * value). The shape of this dot product is [batch, heads, query_len, key_len] 
        output = torch.dropout(output, dropout_p, True)  # Apply dropout to the output. 
        return output


# Initializing the model
m = Model()


