
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        return t1 + t1


# Initializing the model
m = Model()
