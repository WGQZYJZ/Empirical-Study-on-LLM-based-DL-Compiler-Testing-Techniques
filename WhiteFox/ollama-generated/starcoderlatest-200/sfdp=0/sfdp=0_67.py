
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        attention_weights  = self.attention(query=x1, key=x2, value=x2)
        output = attention_weights[0] # First element of the tuple that represents query/value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 3, 64, 64)
