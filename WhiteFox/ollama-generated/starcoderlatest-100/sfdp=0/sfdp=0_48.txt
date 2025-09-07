
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0, "d_model must be divisible by n_heads"

        self.n_heads = n_heads
        self.d_k = d_model // n_heads # Size of each key tensor
        self.d_v = d_model // n_heads # Size of each value tensor
 
        # Weights for query, keys and values
        self.q = torch.nn.Linear(d_model, d_model)
        self.k = torch.nn.Linear(d_model, d_model)
        self.v = torch.nn.Linear(d_model, d_model)
 
    def transpose_for_scores(self, x):
        new_x_shape = x.size()[:-1] + (x.size(-1), x.size(-2) * x.size(-1))
        return x.view(*new_x_shape)

    def forward(self, query, key, value, mask=None):
        # Perform linear projections for the query, keys and values
        batch_size = query.size()[0]
        q = self.q(query).view(batch_size, -1, self.n_heads, self.d_k) # [Batch x Head x Time x Dim_Head x Dim_Key]
        k = self.k(key).view(batch_size, -1, self.n_heads, self.d_k) # [Batch x Head x Time x Dim_Head x Dim_Key]
        v = self.v(value).view(batch_size, -1, self.n_heads, self.d_v) # [Batch x Head x Time x Dim_Head x Dim_Val]

        # Transpose to get [Batch x Time x Head x Dim_Head x Dim_Key]
        q = self.transpose_for_scores(q)  # [Bacth x Time x Head x Dim_Head x Dim_Key]
        k = self.transpose_for_scores(k)  # [Bacth x Time x Head x Dim_Head x Dim_Key]
        v = self.transpose_for_scores(v)  # [Batch x Time x Head x Dim_Head x Dim_Val]
 
        # Scale queries, keys and values to enable dot product attention
        q *= self.d_k ** -0.5
        k *= self.d_k ** -0.5
        v *= self.d_v ** -0.5

        # Compute the dot-product between query, key and value for each head (e.g., batch)
        # [Batch x Head x Time x Dim_Head x Dim_Key] * [Batch x Head x Time x Dim_Head x Dim_Val] => [Batch x Head x Time x Dim_Head x Dim_Val]
        attention_weights = torch.matmul(q, k.transpose(-2, -1)) # [Batch x Head x Time x Dim_Head x Dim_Key] * [Batch x Head x Time x Dim_Key x Dim_Val] => [Batch x Head x Time x Dim_Head x Dim_Val]
 
        # Mask the attention weights to avoid performing unwanted operations on padding token
        if mask is not None:
            mask = (1 - mask) ** 2
            attention_weights = attention_weights + mask

        # Normalize the final attention weights
        attention_weights = nn.Softmax(dim=-1)(attention_weights) # [Batch x Head x Time x Dim_Head x Dim_Val] => [Batch x Head x Time x Dim_Head x Dim_Val]
 
        # Perform weighted sum of all heads using the value (e.g., encoder outputs) as the context vector
        context = torch.matmul(attention_weights, v) # [Batch x Head x Time x Dim_Head x Dim_Val] * [Batch x Head x Time x Dim_Head x Dim_Val] => [Batch x Head x Time x Dim_Head x Dim_Val]
        context = context.transpose(1, 2).contiguous() # [Batch x Head x Time x Dim_Head x Dim_Val] => [Batch x Time x Head x Dim_Head x Dim_Val]
        context = context.view(batch_size, -1, self.n_heads * self.d_v)  # [Batch x Time x Head x Dim_Head x Dim_Val] => [Batch x Time x (Dim_Head x Dim_Val)]
        output = self.o(context)
 
        return output


# Initializing the model
m = MultiheadAttention(d_model=256, n_heads=8)

# Inputs to the model
query  = torch.randn(32, 10, 64) # [Batch x Seq_Len x Dim]
key    = torch.randn(32, 256, 64) # [Batch x Head x Time x Dim]
value  = torch.randn(32, 256, 64) # [Batch x Head x Time x Dim]
mask   = torch.zeros((32, 256), dtype=torch.float32) # [Batch x Head x Time x Dim]
