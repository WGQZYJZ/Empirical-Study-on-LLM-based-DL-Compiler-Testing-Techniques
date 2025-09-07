
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2):
        v1, attention_weights  = self.att(x1, x2, x2) # Apply the attention mechanism
        return v1


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 3, 64, 64)
key = torch.randn(4, 3, 64, 64)
value = torch.randn(4, 8, 64, 64)
