
class Model(torch.nn.Module):
    def __init__(self, query_dim, value_dim):
        super().__init__()

        self.scale = torch.pow(torch.tensor(query_dim), -0.5)
        self.key = nn.Linear(query_dim, query_dim * 32)
        self.value = nn.Linear(value_dim, value_dim * 32)
 
    def forward(self, x):
 
        keys = self.key(x) 
        values = self.value(x)

        scaled_dot_product = torch.matmul(keys, keys.transpose(-2, -1)) / self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights @ values
        return output

# Initializing the model