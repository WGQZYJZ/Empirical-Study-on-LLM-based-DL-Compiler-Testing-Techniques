
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None): # <|>
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2

# Initializing the model
m  = Model()


# Inputs to the model 
# For example: 
x1  = torch.randn(4, 3072) # 
__other__  = torch.randn(4, 59) 

__output__  = m(x1, __other__)