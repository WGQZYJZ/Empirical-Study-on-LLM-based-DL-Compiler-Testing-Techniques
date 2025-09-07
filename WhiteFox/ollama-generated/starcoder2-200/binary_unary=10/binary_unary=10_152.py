
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3


# Initializing the model and generating input tensors to the model
m = Model()
x1  = torch.randn(4, 32)
other  = torch.rand(4, 8).cuda() if device == 'cuda' else torch.rand(4, 8)
 
# Generating outputs from the model with different inputs and passing them to another model (m2 in this case) using `t0`
__output_t1__  = m(x1)


