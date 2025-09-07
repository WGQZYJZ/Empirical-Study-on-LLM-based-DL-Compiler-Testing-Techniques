
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v2 = x1 * 5 + 6
        v1 = self.linear(v2) 
        return torch.addmm(v1, mat_m1, mat_m2).transpose(0, 1)

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(32, 10)

 # Outputs of the model (Note that the model is not fixed in the description and the output is variable) 
