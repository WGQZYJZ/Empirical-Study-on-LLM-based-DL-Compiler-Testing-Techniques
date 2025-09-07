
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.nn.Linear(49037658502, 4903765850)
        v = v(x1)
        v += other # Add another tensor to the output of the linear transformation.
        return v


# Initializing the model
m = Model()
 
# Inputs to the model
