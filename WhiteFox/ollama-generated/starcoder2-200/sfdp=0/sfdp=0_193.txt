
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inv_scale=0.7):
        query = torch.randn(32, 64)
        key = torch.randn(32, 64)
        value = torch.randn(32, 64)
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)

# Initializing the model