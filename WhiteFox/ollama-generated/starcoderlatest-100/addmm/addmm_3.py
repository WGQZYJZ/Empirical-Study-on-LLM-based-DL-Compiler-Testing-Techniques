
class Model(torch.nn.Module):
    def __init__(self, inp_tensor: torch.Tensor):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2) + self.inp
        return v1


# Initializing the model
m = Model(x1)

