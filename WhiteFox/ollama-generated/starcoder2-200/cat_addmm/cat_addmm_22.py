
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2): 
        v1  = torch.addmm(input1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = self.linear(v1)
        return v2

# Initializing the model
m  = Model()

