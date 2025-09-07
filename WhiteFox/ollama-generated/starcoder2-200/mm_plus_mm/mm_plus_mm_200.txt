
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.mm  = torch.mm(input1, input2)

    def forward(self, x3, x4):
        v1 = self.mm(x3, x4)
        return v1


# Initializing the model
m = Model(input_a1, input_a2)
m2  = Model(input_b1, input_b2)
# Inputs to the model
__output__  = m(tensor1, tensor2) + m2(tensor3, tensor4)

