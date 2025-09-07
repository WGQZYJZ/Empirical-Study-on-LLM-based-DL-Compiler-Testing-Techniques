
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1 = torch.mm(x1,y1) # Matrix multiplication between input1 and input2
        return 0.5 * v1


# Initializing the model
m = Model()

# Inputs to the model
__input_x1__=torch.rand(32,34)# Please generate random tensors as inputs here
__input_y1__=torch.rand(34, 8) # Please generate random tensors as inputs here


