
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

 # Initializing the model
m = Model()
__input_tensor__ = torch.randn(3, 10)
