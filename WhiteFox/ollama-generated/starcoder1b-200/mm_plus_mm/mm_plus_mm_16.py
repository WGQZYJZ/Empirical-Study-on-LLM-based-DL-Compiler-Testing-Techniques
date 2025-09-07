
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.MM()
 
    def forward(self, x1, x2):
        v1  = self.mm(x1, x2)
        v2 = torch.matmul(x3, x4) + torch.matmul(x5, x6)  # Matrix multiplication between the input tensors
        return v3


# Initializing the model
m = Model()


