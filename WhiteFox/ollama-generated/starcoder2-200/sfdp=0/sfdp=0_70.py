
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.sqrt(torch.tensor([1024]))
        self.fc1   = torch.nn.Linear(3, 5)
        self.fc2 = torch.nn.Linear(5, 8)
 
    def forward(self, x):
 
        v1  = torch.matmul(x, torch.rand_like(x)) / self.scale 
        v2  = v1.softmax(dim=-1)
        v3  = v2.matmul(torch.rand_like(v2))
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x  = torch.randn(3, 6400, 3).to('cuda')
 
# Forwarding the inputs through the model
__output__  = m(x)

