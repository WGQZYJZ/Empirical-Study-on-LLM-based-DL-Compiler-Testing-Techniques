
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(128, 128)
 
    def forward(self, x1, x2):
        v6 = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(32)
        w  = self.attention(v6) # Scale the input tensor to be between [-1, 1]
        return w


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 128, 32, 32)
x2 = torch.randn(8, 128, 32, 32)
