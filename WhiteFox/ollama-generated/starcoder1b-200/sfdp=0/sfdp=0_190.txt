
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.exp(self.linear2(v1))
        output = (v2 * inv_scale).softmax(-1) @ value

# Initializing the model
m = Model()


