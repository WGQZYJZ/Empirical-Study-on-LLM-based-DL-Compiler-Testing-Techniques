
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2) # 1*2*3 matrix multiplication 
        v4 = v1 + inp # Add the result of this operation to another tensor 'inp' 
        return v6 


# Initializing the model