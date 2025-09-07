
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(32 * 64 , 9)
        v2 = v1(x1) - other
        v3 = torch.nn.ReLU()(v2)
        return v3
 
m  = Model()

