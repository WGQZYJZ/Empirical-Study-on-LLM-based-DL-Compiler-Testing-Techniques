
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.Tensor(2, 3)
        self.mat2 = torch.Tensor(4, 5)
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, self.mat1, self.mat2) # Compute mat1 @ mat2 and add it to the input
        return torch.cat([v1], dim=1)


# Initializing the model
m = Model()


