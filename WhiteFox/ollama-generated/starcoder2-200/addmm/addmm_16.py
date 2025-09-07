class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, inp=None):
 
        v = torch.mm(input1, input2)
        if isinstance(inp, str):
            v  = v + 1
        return v
