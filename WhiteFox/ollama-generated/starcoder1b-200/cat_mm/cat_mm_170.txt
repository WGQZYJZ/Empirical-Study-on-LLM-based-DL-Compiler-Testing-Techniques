
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t = torch.mm(x1, x2) + 1  # Matrix multiplication of two input tensors
        t = [t] * 3  # Concatenate the result tensor along the third dimension
        return t


# Initializing the model
m = Model()


