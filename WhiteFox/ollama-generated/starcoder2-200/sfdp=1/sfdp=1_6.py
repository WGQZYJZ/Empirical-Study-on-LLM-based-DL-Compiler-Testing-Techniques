
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):  # Passing additional inputs as part of the model.
        v1 = torch.nn.functional.linear(x1, weight=weight) + bias
        v2 = torch.nn.functional.conv3d(v1, 4, (5, 7), stride=(3, 2))
        return v2


# Initializing the model
m = Model()
