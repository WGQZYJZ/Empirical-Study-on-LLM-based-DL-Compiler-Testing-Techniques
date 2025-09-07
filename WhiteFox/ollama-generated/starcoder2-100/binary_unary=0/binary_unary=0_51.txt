
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)(x1)
        v5 = torch.nn.MaxPool2d(kernel_size=(4,4))(v1)+torch.nn.Dropout2d()(v1)
        v9 = v1 + other
        v20 = torch.nn.ReLU()(v9)
        return v20


# Initializing the model
m  = Model()
other = m(x1).clone().detach() # Assigning a clone of output of previous model to the 'other' variable, for further use in testing
