
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, n_head, dim):
        super().__init__()
        self.n_head = n_head
        self.dim = dim
        # Attention layer
        self.q = torch.nn.Linear(dim, n_head * 3)  # The query component is multiplied by the head number and added to the key (q + k)
        self.k = torch.nn.Linear(dim, n_head * 3)  # The query component is multiplied by the head number and added to the value (q + v)
        self.v = torch.nn.Linear(dim, n_head * 3)  # Value part of attention
    def forward(self, x1):
        batch_size = x1.shape[0]

        qk = torch.cat([
            self.q(x1),   # Query component: Multiply the input by the head number and added to the key (q + k)
            self.k(x1),   # Query component: Multiply the input by the head number and added to the value (q + v)
            self.v(x1)    # Value part of attention: The same as above
        ], dim=1).view(-1, batch_size, self.n_head, 3 * self.dim)

        qk = qk.transpose(-2, -1)
        
        return self.attention_output(qk)
    
    def attention_output(self, query):
        batch_size = query.shape[0]

        # Attention layer: A multi-head version of the standard self-attention
        att_scores  = torch.einsum("bhqd,bkhd->bhqd", [query, key]) / math.sqrt(key.shape[-1])
        att_weights = F.softmax(att_scores)
        # Attention layer: A single-head version of the standard self-attention
        # attn_output = torch.einsum("bhqd,bkhd->bhqd", [query, key]) / math.sqrt(key.shape[-1])
        # attn_output = F.softmax(attn_output)
        
        return torch.matmul(attn_weights, value).view(-1, batch_size, self.dim)


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head, dim):
        super().__init__()
        self.n_head = n_head
        self.dim = dim

    def forward(self, x1, attn_mask):
        batch_size = x1.shape[0]

        key_values = torch.cat([
            self.q(x1),   # The query component is multiplied by the head number and added to the key (q + k)
            self.k(x1),   # The query component is multiplied by the head number and added to the value (q + v)
        ], dim=1).view(-1, batch_size, self.n_head, 2 * self.dim)

        key_values = key_values.transpose(-2, -1)
        qk = torch.matmul(key_values, self.w).transpose(-2, -1)
        
        return self.attention_output(qk, attn_mask)
    
    def attention_output(self, query, attn_mask):
        batch_size = query.shape[0]

        # Attention layer: A multi-head version of the standard self-attention
        att_scores  = torch.einsum("bhqd,bkhd->bhqd", [query, key]) / math.sqrt(key.shape[-1])
        att_weights = F.softmax(att_scores + attn_mask)
        
        return torch.matmul(attn_weights, value).view(-1, batch_size, self.dim)



# Initializing the model
m = MultiHeadSelfAttention(8, 32)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attn_mask = torch.zeros(1, batch_size, key.shape[-1]) # Attention mask: All values in the attention weights are set to zero except for the diagonal element (which has a value of one), and then the other elements are set to zero.
x2 = m(x1)


# Initializing the model
m = MultiHeadAttention(8, 32)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attn_mask = torch.zeros(1, batch_size, key.shape[-1]) # Attention mask: All values in the attention weights are set to zero except for the diagonal element (which has a value of one), and then the other elements are set to zero.


# Initializing the model
m = FusionSelfAttention(8, 32)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attn_mask = torch.zeros(1, batch_size, key.shape[-1]) # Attention mask: All values in the attention weights are set to zero except for the diagonal element (which has a value of one), and then the other elements are set to zero.


# Initializing the model
m = FusionAttention(8, 32)

# Inputs to the model
x1 = torch.randn(1, 31000f4876666666666666666666666666666666