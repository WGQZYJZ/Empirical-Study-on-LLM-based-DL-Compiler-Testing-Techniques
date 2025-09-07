
class Model(torch.nn.Module):
    def __init__(self, input_size=2048):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()

