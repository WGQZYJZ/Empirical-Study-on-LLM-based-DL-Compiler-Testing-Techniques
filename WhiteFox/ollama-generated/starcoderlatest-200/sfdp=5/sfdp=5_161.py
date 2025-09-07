
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model=1024, num_heads=8):
        super().__init__()

        self.num_heads = num_heads # Number of heads (i.e., number of attention layers in the transformer)
        self.d_model = d_model # Input dimension to transformer model
        self.depth = d_model // num_heads # Depth is equal to `num_heads * head_dim`
        
        # In an input tensor, with shape [batch_size, seq_length, embed_dim], 
        # the output of this layer will have a dimension equal to `num_heads` and `depth`.
        self.qkv = torch.nn.Linear(self.d_model, 3 * self.num_heads * self.depth, bias=False)
        
        self.output_projection = torch.nn.Linear(self.num_heads * self.depth, d_model, bias=True)
 
    def forward(self, x):
        b, s, _ = x.shape  # Shape: [batch_size, seq_length, embed_dim]
        
        qkv = self.qkv(x).reshape(-1, self.num_heads, self.depth, 3)
        query, key, value = torch.chunk(qkv, chunks=3, dim=-1) # Shape: [batch_size, seq_length, embed_dim] x [batch_size, num_heads, depth, embed_dim/num_heads] x [batch_size, num_heads, embed_dim/num_heads]
        
        attn_weight = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.depth)
        attn_weight += 1e-8 # Prevent numerical problems due to division by zero
        
        attn_weight = self._masked_softmax(attn_weight, b, s) 
        output = torch.matmul(attn_weight, value).reshape(-1, self.num_heads * self.depth)
        output = self.output_projection(output) # Shape: [batch_size, seq_length, embed_dim]
        
        return output
 
    def _masked_softmax(self, attn_weight, b, s):  # Shape: [batch_size, num_heads, seq_length, seq_length]
        attn_weight = attn_weight.view(-1, self.num_heads, s, s)
        
        mask = torch.unsqueeze(torch.triu(
            torch.ones((b, self.num_heads, s, s)), diagonal=1).bool(), dim=2)
        attn_weight *= mask
        
        return torch.nn.functional.softmax(attn_weight, dim=-1).view(-1, b * self.num_heads, s, s)
# Initializing the model
m = MultiHeadAttention()


# Inputs to the model
x = torch.randn(1024, 1024, 64)
