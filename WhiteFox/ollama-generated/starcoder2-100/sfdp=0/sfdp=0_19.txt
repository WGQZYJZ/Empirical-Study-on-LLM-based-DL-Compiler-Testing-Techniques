
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1])  # Scaled Dot-Product Attention
        attention_weights = scaled.softmax(dim=-1)  # Compute the softmax of the attention weights 
        output = torch.bmm(attention_weights, value)
 
        return output
 
class MultiHeadAttentionLayer(torch.nn.Module):
    def __init__(self, d_model=256, num_heads=8):
        super().__init__()
 
        self.d_model = d_model  # Size of the model (number of features in the input/output) 
        self.num_heads = num_heads    # Number of attention heads 
 
        self.query_linear = torch.nn.Linear(self.d_model, d_model // self.num_heads * 3)      # Query linear layer
        self.key_linear = torch.nn.Linear(self.d_model, d_model // self.num_heads * 3)        # Key linear layer 
        self.value_linear = torch.nn.Linear(self.d_model, d_model // self.num_heads * 3)      # Value linear layer 
 
        self.scaled_dot = ScaledDotProductAttention()
 
    def forward(self, query, key, value):
 
        # Query is split into multiple chunks based on the number of heads 
        chunked_query = torch.chunk(
            self.query_linear(query),
            chunks=3, dim=-1
        )  # Split it into (d_model // num_heads) three tensors along the last dimension
 
        # Key and Value are also split up into multiple chunks 
        chunked_key, chunked_value = [torch.chunk(x, chunks=self.num_heads, dim=-1) for x in [key, value]]  # Split it into (d_model // num_heads) three tensors along the last dimension
 
        scaled = self.scaled_dot(
            query=chunked_query[0],    # Input to Scaled Dot Product Attention is split into three chunks along the third dimension 
            key=chunked_key[0],        # Keys and Values are also split in this manner 
            value=chunked_value[0]     # 3 Chunks, 1 for query, 1 for keys and another for values
        )
 
        scaled = torch.cat((scaled,) * self.num_heads, dim=-1)   # Concatenate these three chunks along the second dimension
 
        # Convert it back to a single chunk (along the first axis), with d_model channels/features 
        out = scaled.view(
            scaled.shape[0],
            -1
        )
 
        return torch.nn.functional.layer_norm(out, [self.d_model])  # Normalize and return
 
model  = MultiHeadAttentionLayer()

