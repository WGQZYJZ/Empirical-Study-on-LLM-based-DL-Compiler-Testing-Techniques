
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(key)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 3, 64, 64)
key   = torch.randn(2, 8, 64, 64)
