
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.fc = torch.nn.Linear(3 * 64* 64, 8)
 
    def forward(self, x1):
        v2  = torch.max_pooling(x1, 5, stride=2) 
        v3  = torch.mean(v2, dim=[0]) 
        v4  = self.fc(v3)
        return v4

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(8, 3*64 * 64)
__output__  = m(x1)

