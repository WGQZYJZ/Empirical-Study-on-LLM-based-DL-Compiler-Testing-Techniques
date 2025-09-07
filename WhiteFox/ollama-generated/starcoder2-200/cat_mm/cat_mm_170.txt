
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
    
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2  =  # Please fill in this code block
        return v3


# Initializing the model with inputs and running it