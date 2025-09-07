
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*4 + 512*8, 7)
 
    def forward(self, x1):
        v1 = self.linear(x1)
#        v1_other  = torch.randn((3,))
        v2 = v1 + other # Adding another tensor to the output of a linear transformation
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
 x1 = torch.randn(5, 7*4)
 