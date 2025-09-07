
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        v1 = self.attention(query, key, value, scale_factor=inv_scale_factor)
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(16, 32, 24, 32)
