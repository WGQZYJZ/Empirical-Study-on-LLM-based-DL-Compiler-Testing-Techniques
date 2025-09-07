
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(3*64*64, 8)
 
    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = F.relu(v1) # Apply ReLU to the output of the linear transformation
        
        return v2


m2 = Model()

# Inputs to the model
x2  = torch.randn(1,3*64*64)


x2  = torch.randn(100,3*64*64) # For this example we will use a fixed number of input rows (the 100) and generate 3*64*64 input columns to the linear transformation (using the 3*64*64 initial value). You should change it by yourself.
__output2__ = m2(x2) # To be able to check that it is a different model.

