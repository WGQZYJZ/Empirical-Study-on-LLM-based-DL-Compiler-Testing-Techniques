
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8 * 8, 32)
        self.linear2 = torch.nn.Linear(32 + 49 - 6*7 + 5, 8)
 
    def forward(self, x1):
        v0 = x1
        v1 = F.selu(v0)
        v2 = torch.clamp(min=0., max=6., input=F.relu(x1))
        
        l1_input = self.linear1(v2)
        l2_input = torch.nn.functional.pad(l1_input, [3]) 
        v4  = l1_input  + l2_input  - F.elu(-v0) + F.elu(F.relu((-x1)))
        
        l3 = self.linear2(torch.nn.functional.softmax(v4))
        return torch.nn.functional.normalize(l3, p=2.)


# Initializing the model 
m = Model()

# Inputs to the model 
x1 = torch.randn(50) + x1
__output__  = m(x1)