
class MyTransformerModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.input  = torch.randn(1, 50) # Initialize an input tensor to be passed through the transformer model
        self.attn = nn.MultiheadAttention(2048, 64)
 
    def forward(self):
        o1  = self.attn(self.input)[-1]
        o3  = o1 * 5 + torch.randn_like(o1) # Apply a pointwise multiplication operation and then add random noise
        return o3

# Initializing the model
m  = MyTransformerModel()


x2  = m()

# Inputs to the model for both models
x3  = torch.randn(5, 768) # Initialize an input tensor to be passed through the transformer model