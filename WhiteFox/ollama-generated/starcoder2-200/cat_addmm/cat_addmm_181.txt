
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
 
        self.mat1  = torch.tensor([0., 0.], requires_grad=True) if not mat1 else mat1 
        self.mat2  = torch.tensor([0., 0.], requires_grad=True) if not mat2 else mat2
 
    def forward(self, x):
        v3  = torch.addmm(x, self.mat1, self.mat2)
        v4  = torch.cat((v3), dim=-1)
        return v4


# Initializing the model with random weights