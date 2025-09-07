

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1  = torch.nn.Linear(4, 5)
        self.mat2  = torch.nn.Linear(6, 7)
 
    def forward(self, x1):
        v30 = self.mat1(x1[:, [0]])
        v39  = self.mat2(v30).matmul(x1[:, -4:])
        return v39


# Initializing the model