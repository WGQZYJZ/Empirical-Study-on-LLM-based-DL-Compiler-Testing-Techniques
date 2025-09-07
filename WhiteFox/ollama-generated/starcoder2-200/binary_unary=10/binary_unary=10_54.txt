
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48*572, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 + 640
        v4 = F.relu(v3) 
        return v4

m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 572, 893)
