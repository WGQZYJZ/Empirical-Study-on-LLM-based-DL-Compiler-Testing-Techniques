
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.nn.functional.gelu(v1)
        v3 = torch.nn.functional.dropout(v2, p=0.5, training=self.training)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
