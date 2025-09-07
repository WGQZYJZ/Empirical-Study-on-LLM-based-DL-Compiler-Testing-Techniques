
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        return [v1 for i in range(len(v1))]


# Initializing the model
m  = Model()
 

# Inputs to the model
x1  = torch.randn(3, 5) # An input tensor of 3 rows and 5 columns, where each row is a vector
x2  = torch.randn(64, 8) # An input tensor of 64 rows and 8 columns
 
__output__  = m(x1, x2).tolist()

