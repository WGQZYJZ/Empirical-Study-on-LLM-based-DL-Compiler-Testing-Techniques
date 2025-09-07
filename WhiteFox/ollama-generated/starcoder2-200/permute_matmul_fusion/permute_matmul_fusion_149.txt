
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # Permute is invoked twice in one forward definition of a model!
        v1  = torch.permute(x1, (0, 3, 1, 2)) 
        v2  = torch.permute(x2, (0, 4, 5)) # or torch.reshape(x1, (v1.shape[0], x1.shape[-1]))
        v3  = torch.bmm(v1, v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(100, 5000, 4997) # shape of input tensors A and B are not consistent
x2 = torch.randn(100, 3986, 4997)
