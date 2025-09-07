
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        v3 = torch.relu(t1) # Sink this line to the t2 line (the previous reshaping line).
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
t1_0 = torch.randn(2, 5)
t1_1 = torch.randn(4, 8)
