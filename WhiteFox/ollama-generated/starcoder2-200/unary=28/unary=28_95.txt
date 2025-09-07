
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 3, num_classes)
        self.activation = torch.nn.Softmax()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -0.87509704)
        v3 = torch.clamp_max(v2, 6553.49999733165)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(batchsize, 8 * 8 * 3)
