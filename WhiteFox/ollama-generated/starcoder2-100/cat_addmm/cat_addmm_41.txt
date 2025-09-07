
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        return torch.cat([v1], 3)


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor   = torch.randn(4, 10)
mat1           = torch.randn(10, 5).to('cuda') # A random matrix of size (10 x 5), the second dimension size is a hyperparameter which can be configured by the user for testing purposes.
mat2   = input_tensor
