
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1=None, inp=None):
        v1 = torch.mm(input1, inp)
        v2 = v1 + 4
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model: input_tensor and  'inp' tensor that will be added as a keyword argument
input1 = torch.randn(500, 63)
