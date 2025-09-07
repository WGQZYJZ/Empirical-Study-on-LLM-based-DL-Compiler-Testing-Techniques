
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.mm(x1, x1)  # Matrix multiplication of two input tensors
        return torch.cat([t1, t1, ..., t1], dim=-1)


# Initializing the model
m = Model()


