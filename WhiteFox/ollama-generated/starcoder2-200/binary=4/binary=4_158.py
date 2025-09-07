
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + self.__other__
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(4, 512) # 4 samples with 512 dimensions each
other = torch.zeros(4, 1024) # Another tensor of size (4 x 1024) that is not used by the model

 