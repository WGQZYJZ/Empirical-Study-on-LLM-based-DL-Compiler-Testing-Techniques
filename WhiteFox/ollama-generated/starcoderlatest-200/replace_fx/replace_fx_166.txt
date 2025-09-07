 2
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5) # This node is NOT erased! It will NOT trigger the gm.graph.erase_node() line.
        return t1


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(3, 4)
