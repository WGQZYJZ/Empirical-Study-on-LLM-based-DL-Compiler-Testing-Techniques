
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        attention_weights = self.conv.attention(x1, x2)
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
