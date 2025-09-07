
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(1, 8)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = (v1 + ((v1 * v1 * v1)) * 0.044715) * 0.7978845608028654
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = v2 * v5
 
        return v6

# Initializing the model