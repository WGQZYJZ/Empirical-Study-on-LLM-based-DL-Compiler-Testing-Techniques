
class Model(torch.nn.Module):
    def __init__(self, hidden1=256, hidden2=80):
        super().__init__()

        self.fc = torch.nn.Linear(7*7*3, 4)
 
    def forward(self, x1):
        v1  = x1[0]
        v2  = v1 + 3
        v5  = F.relu6(v2 * -99.)
        
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = [torch.randn(7, 7), torch.randn(3)] # Two input tensors
__output__  = m(*x1)