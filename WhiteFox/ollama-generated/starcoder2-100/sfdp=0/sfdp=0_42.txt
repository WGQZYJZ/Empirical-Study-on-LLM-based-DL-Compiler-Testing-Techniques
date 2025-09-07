
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=1024):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # <1>
        attention_weights   = scaled_dot_product.softmax(dim=-1)                    # <2>
        output              = attention_weights.matmul(value)                       # <3>

# Initializing the model