
class Model(torch.nn.Module):
    def __init__(self,  # A tensor used for initialization is introduced here
                 t1=torch.randn(2)):
        super().__init__()

    def forward(self, x):
        v1 = torch.cat([x])
        v2 = v1.view(-1)
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m  = Model()

# Input to the model. The input shape should be equal to that of the tensor used for initialization, which is the shape of the weight matrix of 'linear' layer.
x1 = torch.randn(2)


__output__  = m(x1)
