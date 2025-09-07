
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
query  = torch.randn(8, 256, 512)
key    = torch.randn(8, 256, 512)
value  = torch.randn(8, 2048, 512)
inv_scale = float(256) ** (0.5)

 