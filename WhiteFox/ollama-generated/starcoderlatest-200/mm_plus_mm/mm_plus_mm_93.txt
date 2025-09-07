
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Parameter(torch.randn((4, 3), requires_grad=True)) # The parameter requires gradient to be tracked and updated during optimization, i.e., training the model
        self.mat2 = torch.nn.Parameter(torch.randn((3, 5), requires_grad=True))
 
    def forward(self, x1):
        t1 = torch.mm(x1, self.mat1) # Matrix multiplication between input1 and matrix of weights parameter mat1 (requires gradient to be tracked and updated during optimization, i.e., training the model)
        t2 = torch.mm(x1, self.mat2) # Matrix multiplication between input1 and matrix of weights parameter mat2 (requires gradient to be tracked and updated during optimization, i.e., training the model)
        t3 = t1 + t2 # Addition of the results of the two matrix multiplications
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
