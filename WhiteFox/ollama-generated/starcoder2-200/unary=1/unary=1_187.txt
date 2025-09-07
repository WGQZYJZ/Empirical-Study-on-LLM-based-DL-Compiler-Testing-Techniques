
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 * 0.5
        v3 = (v1 + (v1*v1*v1)*0.044715)
        v4 = torch.tanh(v3)*0.7978845608028654
        v5 = torch.tanh(v4)+1
        return v5


# Initializing the model