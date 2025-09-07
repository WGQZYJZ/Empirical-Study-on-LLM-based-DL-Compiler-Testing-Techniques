
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        return v + [v for _ in range(3)]


# Initializing the model
m = Model()

