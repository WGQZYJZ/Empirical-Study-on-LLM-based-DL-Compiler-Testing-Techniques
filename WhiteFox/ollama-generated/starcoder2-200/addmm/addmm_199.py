
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 +  inp # where 'inp' is the second input tensor that is passed as a keyword argument during inference. 
        return v2


# Initializing the model