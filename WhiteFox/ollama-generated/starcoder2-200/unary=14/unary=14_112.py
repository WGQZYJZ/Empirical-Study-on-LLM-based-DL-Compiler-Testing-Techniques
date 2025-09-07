
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self._convtranspose(x1)
        v2  = torch.sigmoid(v1)
        return v2 * v1

# Initializing the model with a different random seed for each call to torch.manual_seed()
torch.manual_seed(0)

