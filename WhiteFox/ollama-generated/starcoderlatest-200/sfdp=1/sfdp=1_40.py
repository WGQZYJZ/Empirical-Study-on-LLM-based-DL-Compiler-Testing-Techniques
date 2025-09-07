
class Model(torch.nn.Module):
    def __init__(self, dim_attention_key: int = 128):
        super().__init__()
 
        self.dim_attention_key = dim_attention_key
 
        # Define a multi-head dot product attention mechanism with the number of heads set to 2
        self.multihead_attn = torch.nn.MultiheadAttention(input_dim=self.dim_attention_key, num_heads=2)
 
    def forward(self, query, key, value):
        qk, _ = self.multihead_attn(query, key, value)
        return qk
