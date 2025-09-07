
class Model(torch.nn.Module):
    def __init__(self, inv_scale=8):
        super().__init__()
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output              = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 8, 64, 64)
key   = torch.randn(2, 8, 32, 32)
value = torch.randn(2, 8, 64, 64)
