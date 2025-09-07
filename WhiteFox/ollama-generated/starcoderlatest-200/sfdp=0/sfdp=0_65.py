
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 512) # A linear layer with input dim=32 and output dim=512
        self.key = torch.nn.Linear(32, 512)
        self.value = torch.nn.Linear(32, 512)
 
    def forward(self, x1):
        query = self.query(x1).unsqueeze(-2) # Query is a single vector, so add one more axis for broadcasting
        key = self.key(x1) 
        value = self.value(x1)
 
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (key.size()[-1] ** 0.5) # In the Scaled Dot-Product Attention mechanism, the scale of query/key vectors should be same as value
        attention_weights = scaled_dot_product.softmax(dim=-1) # Compute the softmax attention weights with dim=-1 
        output = torch.matmul(attention_weights, value)
 
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 32, 64, 64)
