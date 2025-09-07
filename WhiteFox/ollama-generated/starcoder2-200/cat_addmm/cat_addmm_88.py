
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1  = torch.addmm(x1, mat1, mat2)
        return t1

 # Inputs to the model