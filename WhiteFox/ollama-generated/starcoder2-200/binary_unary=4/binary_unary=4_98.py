
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(5, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.ones(v1.shape).to('cuda') 
        v3  = F.relu(v2) # The ReLU activation function is applied to the result
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(5, 4).to('cuda')


