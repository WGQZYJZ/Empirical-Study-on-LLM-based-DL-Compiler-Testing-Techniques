
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # This forward function contains only torch functional calls and uses a single input tensor, which is the original input tensor passed to the model for inference.
        t2 = torch.rand_like(x1) 
        return torch.nn.functional.dropout(t2, ...)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(3)
 
