
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(512, 8)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Attention()


# Inputs to the model
query = torch.randn(8, 512, 64, 64)
key   = torch.randn(8, 512, 64, 64)
value = torch.randn(8, 512, 64, 64)
