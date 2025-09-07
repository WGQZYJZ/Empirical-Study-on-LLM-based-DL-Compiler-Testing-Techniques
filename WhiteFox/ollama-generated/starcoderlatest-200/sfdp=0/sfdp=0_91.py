
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(32*7*7, 3)
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 32*7*7, 64, 64)
key   = torch.randn(1, 3, 32*7*7, 64)
value = torch.randn(1, 8, 32*7*7, 64)
inv_scale  = math.sqrt(32*7*7)
