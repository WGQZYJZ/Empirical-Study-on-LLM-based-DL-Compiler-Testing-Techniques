
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.split(x1, [8], 1) # Split the input tensor along dimension `i` into eight tensors
        v1 = torch.cat([v0[i] for i in range(len(v0))], 2) # Concatenate these split tensors along dimension 3
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model 
x1 = torch.randn(1, 8, 64, 64)
__output__  = m(x1)