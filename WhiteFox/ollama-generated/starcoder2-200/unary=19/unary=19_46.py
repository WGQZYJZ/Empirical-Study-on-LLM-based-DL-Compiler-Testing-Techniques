
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 64*64*3))
        v2 = torch.sigmoid(v1) # sigmoid function is not implemented in TorchScript
        return v2


# Initializing the model