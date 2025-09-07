
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        v1 = torch.rand_like(input_tensor, ...) # Generate a tensor with the same size as input_tensor filled with random numbers
        return self.dropout(v1)


# Initializing the model and adding replace nodes in the graph 
m = Model()
gm.graph.replace_fx_in_module('rand_like', 'lowmem_dropout')


# Inputs to the model, after applying replacement on input nodes (with replace_fx set as True)
x1 = torch.randn(1, 2, 2)
