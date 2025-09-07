
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        return torch.nn.functional.conv2d(x1, conv)
m = Model()
__output__  = m(input_tensor)


# Initializing the model and inputs to the model