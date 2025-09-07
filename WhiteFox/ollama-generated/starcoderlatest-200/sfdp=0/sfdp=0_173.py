
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(512, 512)
 
    def forward(self, query, key):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(self.key(value))
        return output

# Initializing the model
m = Model()

 # Inputs to the model
    query  = torch.randn(5, 32, 48, 96)
    key    = torch.randn(10, 32, 48, 96)

    