
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.tanh(v1) # <--- Add this line and the following line after torch.tanh()
        v3  = v2 + 3   # <--- This line is added to check if torch.add_n() is used
        return v3, v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(80)
__output__, __intermediate_variable__  = m(x1)

# The intermediate variable will be added as an input tensor to another model that you implement

