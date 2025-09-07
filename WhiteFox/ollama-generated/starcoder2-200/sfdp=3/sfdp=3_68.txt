
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Linear(256, 3072)
 
    def forward(self, kq):
        v1 = self.mat1(kq) 
        return v1

# Initializing the model