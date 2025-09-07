
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = torch.nn.Linear(8*8*3, 2)(x1)
        v1 -= 0.5
        v1 += other
        v1 = torch.nn.ReLU()(v1)
        return v1
 
# Initializing the model
m = Model()

