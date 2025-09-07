

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 256) 
        self.linear2 = torch.nn.Linear(256, 300) 
        self.linear3 = torch.nn.Linear(300, 400)
 
    def forward(self, x1):
        v1 = F.relu(self.linear1(x1)) 
        v2 = F.dropout(v1, p=0.5) # Apply dropout to the output of linear1 with probability 0.5
        v3 = self.linear2(v2) 
        v4 = F.relu(v3)
        v5 = F.elu(self.linear3(v4))# Apply exponential linear unit to the output of linear3 and then add the original input as the output
        v6  = v1 + v5
        return v6, torch.nn.BatchNorm2d(input=v6, affine=True)

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8,784)
__output__, __layer_4_output__  = m(x1)

