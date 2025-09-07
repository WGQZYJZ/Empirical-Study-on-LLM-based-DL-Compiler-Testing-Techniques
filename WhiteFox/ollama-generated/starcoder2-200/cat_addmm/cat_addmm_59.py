
class Model(torch.nn.Module):
    def __init__(self, num1, num2):
        super().__init__()
 
        self.mat1 = torch.zeros((3072, 48)) 
        self.mat2 = torch.randn(48, 96)
        self.linear = torch.nn.Linear(3072 + 48, 96)
 
    def forward(self, x):
 
        m1  = torch.addmm(x, self.mat1, self.mat2)
        return m1

# Initializing the model
m  = Model()

 # Inputs to the model
__inputs__ = [
    torch.randn(64, 3072), 
    torch.randn(96)
]

