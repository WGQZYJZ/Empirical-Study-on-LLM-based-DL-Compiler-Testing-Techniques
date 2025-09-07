
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1):
        v2  = torch.rand_like(x1).to(x1.device)  # The input to the model is filled with random numbers
        v3  = torch.nn.functional.dropout(v2, p=0.5, training=True)

        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4).to('cuda') # The inputs are randomly generated with size [N] and the dtype is float
__output__  = m(x1)

