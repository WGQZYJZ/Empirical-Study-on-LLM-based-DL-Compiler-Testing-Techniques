

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(*x1.shape)  # Create a new tensor with the same size as an input tensor

        v3 = v2 + self.__output__   # Add another tensor to the output of the linear transformation

        return v3

# Initializing the model
m = Model()


# Inputs to the model