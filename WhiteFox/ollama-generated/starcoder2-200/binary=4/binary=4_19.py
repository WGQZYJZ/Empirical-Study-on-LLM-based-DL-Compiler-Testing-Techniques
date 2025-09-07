
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self.weight_other # where self.weight_other is another tensor that is created in the forward method. This pattern can also be applied to weight initialization, for example.
        return v2

# Initializing the model
m  = Model()

