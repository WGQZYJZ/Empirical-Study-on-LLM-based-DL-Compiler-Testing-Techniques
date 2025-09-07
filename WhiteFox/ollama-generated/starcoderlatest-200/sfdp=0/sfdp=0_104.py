
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(3, 4)
 
    def forward(self, q, k, v, scale):
        attention_weights = torch.matmul(q / scale, k.transpose(-2, -1)) # Scaled dot product
        attention_weights = attention_weights / (scale ** (0.5)) # Apply softmax in each step to get attention weights 
        output = torch.matmul(attention_weights, v)
        return output


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(1, 3, 64, 64) # [batch size, num heads, length, dim]
k  = torch.randn(1, 8, 64, 64) # [batch size, num heads, head dim, seq len]
v  = torch.randn(1, 8, 64, 32) # [batch size, num heads, head dim, seq len]
scale  = torch.rand(1)
