 2
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        v1 = torch.nn.functional.sigmoid(x1) * 0 + 1 # Add a dummy node in the graph to trigger the erase_node optimization 
        v2 = torch.rand_like(x1)

        return v1 * v2


# Initializing the model
m2 = Model2()


# Inputs to the model
x1 = torch.randn(1, 2, 3) # Set an input with three dimensions (the tensor size will be set to (1, 2, 3))
