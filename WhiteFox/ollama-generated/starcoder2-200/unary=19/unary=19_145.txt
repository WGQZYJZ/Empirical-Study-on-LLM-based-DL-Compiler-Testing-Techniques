
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64*64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1.reshape(-1)) 
        v2  = torch.sigmoid(v1)
        return v2
# Initializing the model
m  = Model()
 
# Inputs to the model
input_tensor = torch.randn(32, 64*64).view(1,-1)
 
# __output__  = m(input_tensor)

