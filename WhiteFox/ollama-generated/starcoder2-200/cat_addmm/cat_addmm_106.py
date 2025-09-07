
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 64 + 63085273728, 9)
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
 
        t1  = matmul(x1, mat1) 
        t2  = matmul(mat2, t1)
        t3  = torch.cat([t2], dim)
        return t3


# Initializing the model
m  = Model()

