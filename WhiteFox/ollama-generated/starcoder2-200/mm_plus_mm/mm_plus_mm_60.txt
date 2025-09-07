
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1: torch.Tensor,
                 input2: torch.Tensor,
                 input3: torch.Tensor,
                 input4: torch.Tensor) -> torch.Tensor:
 
        v1 = torch.mm(input1,  input2) 
        v2 = torch.mm(input3,  input4)
        return v1 + v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(780, 90567) # Input data for Matrix Multiplication 1
x2 = torch.randn(39423, 90567) # Input data for Matrix Multiplication 2
x3 = torch.randn(780, 90567) # Input data for Matrix Multiplication 3
x4 = torch.randn(39423, 90567) # Input data for Matrix Multiplication 4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(780, 90567) # Input data for Matrix Multiplication 1
x2 = torch.randn(39423, 90567) # Input data for Matrix Multiplication 2
x3 = torch.randn(780, 90567) # Input data for Matrix Multiplication 3
x4 = torch.randn(39423, 90567) # Input data for Matrix Multiplication 4

