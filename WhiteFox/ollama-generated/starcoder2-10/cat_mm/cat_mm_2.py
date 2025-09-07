
class Model(torch.nn.Module):
    def __init__(self, list1):
        super().__init__()
 
    def forward(self, input1, input2):
        v0  = [input1] * len(list1) # List multiplication of an input tensor and a given number of times
        v1  = torch.cat(v0 + [torch.zeros([len(list1), len(list1)], dtype=input2.dtype)])
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64)
x2 = torch.randn(64)
__output__  = m(x1, x2)

