
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.key = torch.nn.Linear(dim, dim)
        self.query = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
 
    def forward(self, query_vector):
        key  = self.key(query_vector)
        value  = self.value(query_vector)
        scaled_dot_product  = torch.matmul(key, self.query(query_vector).transpose(-2, -1)) / sqrt_dim 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
 
        return output


# Initializing the model
m  = Attention(512)
 
# Inputs to the model
query  = torch.randn(3, 800, 768)
 
 
