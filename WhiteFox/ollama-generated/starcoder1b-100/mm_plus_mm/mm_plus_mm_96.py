
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + torch.mm(x2, x1)  # Matrix multiplication of two matrices with addition


# Initializing the model
m = Model()


