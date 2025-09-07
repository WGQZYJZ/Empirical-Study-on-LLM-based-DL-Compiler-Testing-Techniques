
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x2) # Matrix multiplication between the input at index 0 and the input tensor in x2
        v2  = torch.mm(x3[0], x4[0]) # Matrix multiplication between the input at index 0 of the input tensors in x3 and the first element (index 0) of the input tensors in x4
        return v1 + v2


# Initializing the model
m = Model()


