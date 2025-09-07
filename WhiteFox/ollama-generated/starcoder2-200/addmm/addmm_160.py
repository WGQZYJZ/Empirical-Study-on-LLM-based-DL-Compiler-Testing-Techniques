

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2=None, **kwarg):
        v1 = torch.mm(input1, input2) + kwarg['inp'] 
        return v1


# Initializing the model