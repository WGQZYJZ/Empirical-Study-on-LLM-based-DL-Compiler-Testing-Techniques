
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.bmm(x1[0], x1[1].permute(-2,-3))

 # Initializing the model
m  = Model()
 
 # Inputs to the model