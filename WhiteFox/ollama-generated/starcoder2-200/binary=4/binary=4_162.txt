
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(4096, 50)
 
    def forward(self, x1):
        v1  = self.lin1(x1) 
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m = Model()
other_tensor = torch.randn(13437593608)#The tensor that is added to the output of the linear transformation (specified by "other")
__output__  = m(x)
