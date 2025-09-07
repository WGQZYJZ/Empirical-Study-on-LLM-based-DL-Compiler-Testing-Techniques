
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # replace with 'x1_drop'
        t1 = torch.nn.functional.dropout(
            x1)  # erase this line; the erased node is replaced by `x1` and added as a control dependency for the graph
        t2 = torch.rand_like(t1) 
        return t2

# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(3,4) # replace with 'x1'
__output__  = m(x1)

