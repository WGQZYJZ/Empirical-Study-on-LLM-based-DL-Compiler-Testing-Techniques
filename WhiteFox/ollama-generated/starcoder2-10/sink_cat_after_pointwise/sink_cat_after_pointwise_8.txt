
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1  = torch.cat([x1[0], x1[3]], dim=...) # Concatenate along axis 1
        t2  = t1.view(-1, ...) # Reshape the concatenated tensor
        t3  = torch.relu(t2) # Apply ReLU to the reshaped tensor
        return (t3, )


# Initializing the model
m  = Model()


# Inputs for the model
x1_data  = [torch.randn(4), torch.randn(4)]
__output__  = m(*x1)

