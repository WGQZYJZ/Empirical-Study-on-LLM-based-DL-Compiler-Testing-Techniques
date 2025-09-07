
class Model(torch.nn.Module):
    def __init__(self, inp = None):
        super().__init__()
        self.matmul1 = torch.nn.Linear(32, 8)
        self.mat1 = torch.nn.Conv2d(32, 8, 1, stride=1, padding=0)
 
        if inp is not None:
            assert inp == 5
 
    def forward(self, x):
        v1 = self.matmul1(x)
        v2 = self.mat1(v1)
        