

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4 * 64, 8)
    
    def forward(self, x1):
        v1  = self.linear(x1.reshape(-1, 4*64)) 
        v2  = F.sigmoid(v1) # We can add F for backward compatibility
        v3  = v1 * v2
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 64).unsqueeze(-1)

__output__  = m(x1)

