
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor # Here we pass another tensor named `other_tensor` as a keyword argument 
        return v3


# Initializing the model