
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(256, 3072)
 
    def forward(self, x1):
        v1 = self.l1(x1)
        v2 = v1 * F.relu6(v1 + 3) / 6
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(256, 4098) # A random tensor with size [batch_size x input_features]

