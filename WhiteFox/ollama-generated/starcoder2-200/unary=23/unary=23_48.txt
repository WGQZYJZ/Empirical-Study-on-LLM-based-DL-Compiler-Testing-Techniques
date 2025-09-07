
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v0  = torch.randn(256)
         v1  = v0 - self.__constant__
         v3  = x1[v1]
         return x1,v3
 
 # Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1024,16)

 # Outputs of the model on different inputs. The first output is the same for all input tensors.
outputs  = m(x1)


