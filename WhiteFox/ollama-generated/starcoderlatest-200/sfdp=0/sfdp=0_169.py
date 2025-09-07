
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4) 
        self.key   = torch.nn.Linear(4, 8)
 
    def forward(self, x1, x2):
        attention_weights  = torch.matmul(self.query(x1), self.key(x2).transpose(-2, -1)) / (x2.size()[1]**0.5) # Scale dot-product by square root of key size in embedding dimension
        attention_weights  = attention_weights.softmax(dim=-1)
        output = torch.matmul(attention_weights, self.value(x2))
        return output
 
    def value(self, x):
        return torch.nn.Linear(8, 3)(x)
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 4, 64, 64)
