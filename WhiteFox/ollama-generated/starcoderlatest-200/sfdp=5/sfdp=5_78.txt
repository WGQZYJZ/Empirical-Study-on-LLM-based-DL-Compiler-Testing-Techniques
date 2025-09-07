
class SelfAttentionModule(torch.nn.Module):
    def __init__(self, n_heads=8, d_model=64, d_k=64, d_v=64):
        super().__init__()
        self.n_heads = n_heads
        self.d_model = d_model
        self.d_k = d_k
        self.d_v = d_v
        
        # A query, key, and value for each attention head is required to calculate the attenion weights
        self.query = torch.nn.Linear(d_model, n_heads * d_k, bias=False)
        self.key = torch.nn.Linear(d_model, n_heads * d_k, bias=False)
        self.value = torch.nn.Linear(d_model, n_heads * d_v, bias=False)
        
        # After computing the attention weights (with softmax and dropout), the output is multiplied by a constant for all heads and summed up. The resulting tensor has shape (batch size, sequence length, hidden dimension).
        self.attn = torch.nn.Linear(n_heads * d_v, n_heads * d_model, bias=False)
    
    def forward(self, input):
        batch_size, seq_len, _ = input.shape  # Get the shape of inputs from the tensor `input`.
        head_dim = self.d_k // self.n_heads  # Set the dimension size of attention heads to be computed in a linear layer (i.e., hidden dim = `head_dim * n_heads`)
        
        # Compute query and key using `self.query`, `self.key` to transform the inputs
        q = self.query(input)
        k = self.key(input)
        
        # Multiply the keys by square roots of their dimensions (dividing them to scale their dot product) in order to compute attention weights from scaled dot products, then divide them again with the square root of attention heads (`head_dim`) for final output and then apply softmax operation
        attn_weight = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        attn_weight = torch.softmax(attn_weight, dim=-1)
        
        # Dropout the attention weights before concatenating heads in a linear layer (i.e., `n_heads` heads ->  `n_heads * head_dim`) to get the output from the last convolutional layer
        attn_weights = torch.dropout(attn_weight, dropout_p)
        output = torch.matmul(attn_weights, self.value(input))
        
        # Concatenate heads for each attention head in a linear layer (i.e., `n_heads * head_dim` ->  `n_heads * d_v`) to get the final output of transformer model.
        output = torch.transpose(output, -2, -1).contiguous().view(batch_size, seq_len, self.n_heads * head_dim)
        output = self.attn(output)
        
        # Output tensor has shape (batch size, sequence length, hidden dimension), which is required by `torch.nn.Linear` layer to compute the final outputs for transformer model. This transformation is performed before and after `self-attention module`.
        return output


# Initializing the model
m = SelfAttentionModule()


# Inputs to the model
x1 = torch.randn(1, 64, 64)
