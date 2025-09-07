
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, replace=True):
        v2 = torch.nn.functional.dropout(x1, p=0.25, inplace=replace)  # Replace by lowmem_dropout() function
        if replace:
            x2 = torch.rand_like(v2) 
        else: 
            x2 = v2
        return x2

# Initializing the model
m = Model()


x1 = torch.randn(4, 20)  # Replace by lowmem_dropout with probability p=0.25
x2 = m(x1)

# After this line is run, the graph should look like:
gm.get_node("lowmem_dropout", 3).type == "call"   # lowmem_dropout() is called in the third call node of the graph

