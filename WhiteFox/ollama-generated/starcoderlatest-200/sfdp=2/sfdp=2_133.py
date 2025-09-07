
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1, x2):
        v1 = torch.nn.functional.relu(self.linear(x1))
        v2 = torch.nn.functional.sigmoid(self.linear(x2))
        return (v1 * x1), (v2 * x2)


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 512)
key = torch.randn(1, 512)
value = torch.randn(1, 512)
