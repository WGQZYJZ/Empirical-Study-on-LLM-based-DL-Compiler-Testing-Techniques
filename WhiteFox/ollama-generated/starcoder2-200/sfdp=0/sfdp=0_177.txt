
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(3)
        v3  = scaled_dot_product + 0.5
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8, 8)
