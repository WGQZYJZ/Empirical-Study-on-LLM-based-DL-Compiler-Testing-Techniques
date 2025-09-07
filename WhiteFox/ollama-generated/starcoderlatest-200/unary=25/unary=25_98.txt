
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * -1 # multiply by negative slope value here
        return torch.where(v1, v2, v1 * 0.7071067811865475)
# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64) # input tensor
