
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 100)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # where 'other' is a constant that was previously determined
        v3 = torch.relu(v2) 
        return v3


# Initializing the model and generating input data
m  = Model()
 
input_data  = torch.randn(10, 32)
__output__  = m(input_data)
