
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1  = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1  = self.mm1(x1)
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
input1  = torch.randn(20, 8) # 1st input tensor of shape (20, 3) - number of rows must be 5 or more
input2  = torch.randn(3, 4) # second input tensor with shape (3, 4), 8 or less rows required by the matrix multiplication operation
input3  = torch.randn(16, 8) # 3rd input tensor of shape (16, 3) - number of columns must be 5 or more
input4  = torch.randn(20, 8) # 4th input tensor with shape (3, 16), 8 or less columns required by the matrix multiplication operation
 
__output__  = m(x1)

