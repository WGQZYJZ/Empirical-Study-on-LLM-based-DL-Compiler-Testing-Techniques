

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 128)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = nnf.relu(v1)
        return v2

m  = Model()

 # Inputs to the model 
 x = torch.randn(1, 64*64)
 
 