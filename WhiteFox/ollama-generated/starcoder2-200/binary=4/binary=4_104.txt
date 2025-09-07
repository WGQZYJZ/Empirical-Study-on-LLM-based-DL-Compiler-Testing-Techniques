
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.empty(3, 4) # Creating an empty tensor with three rows and four columns 
        v2 = v0 + torch.ones_like(v0) * 100 # Adding another tensor to the output of the linear transformation
        return v2


# Initializing the model