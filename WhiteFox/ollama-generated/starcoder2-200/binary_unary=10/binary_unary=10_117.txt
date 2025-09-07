
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048*3 * 7, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) + other_tensor
        v2  = F.relu(v1) # or v2 = relu(v1)
        return v2


# Initializing the model and inputs to the model
m   = Model()
x1  = torch.randn(3, 2048*7)
__output__  = m(x1)