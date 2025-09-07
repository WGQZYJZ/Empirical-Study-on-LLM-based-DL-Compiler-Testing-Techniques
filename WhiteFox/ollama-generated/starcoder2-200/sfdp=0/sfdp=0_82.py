
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layernorm1 = torch.nn.LayerNorm([256])
        self.fc1  = torch.nn.Linear(784, 30)
 
    def forward(self, x1):
        v1  = self.layernorm1(x1)
        v2  = v1 * x1.view(-1) + x1.sum()
        return v2

# Initializing the model