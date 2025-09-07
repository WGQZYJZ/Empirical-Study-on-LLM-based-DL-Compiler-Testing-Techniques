
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.FullPad2d(pad=0, value=1)
 
    def forward(self, x1, x2):
        v1 = self.full(x1, x2)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # [batch_size x channels x height x width]
x2 = torch.randn(1, dtype=torch.int32) # A scalar that specifies the size of dimension 0 for the output tensor
