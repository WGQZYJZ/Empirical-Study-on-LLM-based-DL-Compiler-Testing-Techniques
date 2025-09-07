
class Attention(torch.nn.Module):
    def __init__(self, dim=16):
        super().__init__()
        self.scale = math.sqrt(dim)
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model
attn = Attention()

