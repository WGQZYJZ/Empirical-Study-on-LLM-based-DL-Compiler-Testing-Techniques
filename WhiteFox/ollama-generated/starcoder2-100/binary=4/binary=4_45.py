
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(25088, 6)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        return v1 + 5


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(2048*6*32*32, requires_grad=True).reshape(-1, 32, 32) # The input tensor has a shape of [2048 * 6] because the number of inputs (flattened channels) is 5184
 
