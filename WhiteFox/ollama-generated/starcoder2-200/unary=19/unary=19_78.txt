
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 1)
 
    def forward(self, x):
        v1 = self.linear(x) # Linear transformation with input size [N, 32*64*64] and output size [N, 1]
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model