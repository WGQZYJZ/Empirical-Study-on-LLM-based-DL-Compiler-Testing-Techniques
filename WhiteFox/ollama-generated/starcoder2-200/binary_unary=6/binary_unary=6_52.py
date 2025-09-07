class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 32)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return self.relu(v2)
m  = Model()
__input_tensor__= torch.randn(3,4)
x1 = torch.randn(10, 4)
