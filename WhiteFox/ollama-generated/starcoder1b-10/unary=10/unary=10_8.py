
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + 3

    @staticmethod
    def scaled_activation(x, scale=1.0):
        