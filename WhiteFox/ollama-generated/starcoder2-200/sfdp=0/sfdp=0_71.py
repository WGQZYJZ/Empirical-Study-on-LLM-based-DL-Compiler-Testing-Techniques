
class Attention(torch.nn.Module):
    def __init__(self, dim=32, scale=1):
        super().__init__()

        self.scale = scale
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / self.scale 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)

        return output

# Initializing the model
model = Attention()

