
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + other_tensor # A tensor that is not directly used by the model
        v3  = torch.relu(v2) # Applying ReLU on output of linear transformation to v2
        return v3


# Initializing the model
m  = Model()
other_tensor=torch.randn(1,8)# Initialize another tensor with random values

# Inputs to the model
x1  = torch.randn(1, 32)
__output__  = m(x1)