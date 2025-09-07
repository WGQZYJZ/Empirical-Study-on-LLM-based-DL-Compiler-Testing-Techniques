
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4096 + 2, 38)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2  = v1  + other_tensor
        v3 = F.relu(v2) # F is the ReLU activation function in torch.nn.functional
        return v3
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(64, 9705) + other_tensor 
 
