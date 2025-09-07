
class Model(torch.nn.Module):
    def __init__(self,  **kwargs):
        super().__init__()

    def forward(self, x1,  **kwargs):
        v1 = torch.mm(x1, kwargs['v']) + self.__output__
        return v1

 # Initializing the model
m = Model()
 
 # Inputs to the model: one input tensor and a keyword argument dictionary with a key `v` whose value is an input tensor used in matrix multiplication
x1  = torch.randn(4,5)
  kwargs = {'v':torch.randn(4,5)}
 
 # Initializing the output of the model
 