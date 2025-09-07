

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args):
        t0 = torch.cat([i for i in args], dim=1)
        t3 = t0[:, 0:size] # Slice the first tensor along dimension 1 to a fixed size and return the sliced output.
        t4 = torch.cat([t0, t3], dim=1) # Concatenate input tensors with their sliced outputs together along dimension 1.
        return t4


# Initializing the model
m = Model()


# Inputs to the model
_inputs  = [torch.randn(256)] * 20
__output__  = m(* _inputs)
