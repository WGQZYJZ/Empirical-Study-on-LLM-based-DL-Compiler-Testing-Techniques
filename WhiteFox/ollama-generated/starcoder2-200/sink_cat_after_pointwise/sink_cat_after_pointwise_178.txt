
class Model(torch.nn.Module):
    def __init__(self, num_inputs=3):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        t1  = torch.cat([x1] * 50 + [torch.randn(4)]) # Concatenate tensors along the first dimension and then apply a pointwise unary operation to it 
        t2  = self.linear(t1)
        return t2

# Initializing the model
m = Model()

