
class Model(torch.nn.Module):
    def __init__(self, out_dim):
        super().__init__()
        self.linear = torch.nn.Linear(3, out_dim)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2

# Initializing the model and generating an input tensor for the new one
m  = Model(out_dim=8)
input = torch.randn(1, 3, 64, 64)

