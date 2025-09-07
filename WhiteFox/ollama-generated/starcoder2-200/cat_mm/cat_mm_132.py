
class Model(torch.nn.Module):
    def __init__(self, input1=50):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1] * input1, dim=-3)
        return v2


# Initializing the model and generating the inputs to the model