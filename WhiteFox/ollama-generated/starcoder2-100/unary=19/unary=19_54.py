

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.sigmoid(v1) 
        return v2

m  = Model()

# Inputs to the model
input_tensor = torch.randn(4,5)
output__  = m(input_tensor)

