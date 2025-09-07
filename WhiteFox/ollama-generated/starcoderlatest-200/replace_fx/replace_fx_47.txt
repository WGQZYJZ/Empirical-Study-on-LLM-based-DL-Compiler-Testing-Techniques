
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, self.p) # The input tensor will be replaced with the corresponding `lowmem_dropout`
        t2 = torch.rand_like(x1) # A new random tensor is generated to replace the input tensor. 
        return t1, t2
m = Model()
## Set the following two configuration options in config_graphmutator_model
self.p = 0.5
self.replace_fx = ['torch.nn.functional.dropout', 'torch.rand_like']
# Initialization: The input tensor of the dropout function is passed as an argument here.


# Inputs to the model
x1 = torch.randn(2, 3, 4)
