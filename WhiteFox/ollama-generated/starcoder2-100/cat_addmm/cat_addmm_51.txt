
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc = torch.nn.Linear(28 * 28 + 50, 1)
        self.dim = dim
 
    def forward(self, x1):
        t1  = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t3  = t1[torch.randperm(t1.shape[-2]), :, :]
        t4  = torch.nn.functional.relu(t1) 
        t5  = t4 + self.fc(x1)
 
        return t5

# Initializing the model
m  = Model(3)

 # Inputs to the model
x1  = torch.randn(20, 784)
 
 __output__  = m(x1)