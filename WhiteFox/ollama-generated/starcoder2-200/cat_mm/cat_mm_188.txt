
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x):  # A forward pass function of the model
        t = torch.mm(input1, input2)  # Matrix multiplication of two input tensors
        t2 = torch.cat([t for i in range(3)], dim=0) 
        return t


# Initializing the model with different inputs to the model.
m = Model(torch.randn(4, 5), torch.randn(6,7))


