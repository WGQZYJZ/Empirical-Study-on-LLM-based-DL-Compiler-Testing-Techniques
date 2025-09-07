
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2) # Matrix multiplication of two input tensors
        return torch.cat([v1] * 5000, dim=3).sum()

# Initializing the model
m = Model()

