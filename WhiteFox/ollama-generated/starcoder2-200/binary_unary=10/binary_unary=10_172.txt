
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 50)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + other # other is another random tensor
        v3  = F.relu(v2)  
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(50, 64 * 64 * 3)

 # Please add random tensors as follows:
other  = torch.randn(1, 32)
 
__output__  = m(x1)


