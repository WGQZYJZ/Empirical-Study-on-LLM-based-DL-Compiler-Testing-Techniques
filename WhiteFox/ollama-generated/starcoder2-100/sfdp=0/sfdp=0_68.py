
class SelfAttention(torch.nn.Module):
    def __init__(self, dim=768):
        super().__init__()
        self.scale = 1 / math.sqrt(dim)
 
    def forward(self, query, key, value):
        # Scaled dot-product attention
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(value)
        return output

# Initializing the model
sa = SelfAttention()

 # Inputs to the model
query   = torch.randn(32, 64, 768)
key     = torch.randn(32, 5120, 768)
value    = torch.randn(32, 5120, 768)
 
__output__  = sa(query, key, value)

