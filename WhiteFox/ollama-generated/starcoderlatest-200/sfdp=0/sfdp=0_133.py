
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=1024, num_heads=8)
 
    def forward(self, x1):
        attention_output, attention_weights  = self.attention(x1, x1, x1)
        return attention_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256, 1024, 8, 3)
