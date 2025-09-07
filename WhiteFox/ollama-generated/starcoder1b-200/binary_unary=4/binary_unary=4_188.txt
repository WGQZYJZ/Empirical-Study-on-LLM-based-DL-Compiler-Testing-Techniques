
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1) + kwargs['other']
        return relu(v1)


# Initializing the model
m = Model()


