
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, inp):
        v1 = torch.mm(input1, inp) # Matrix multiplication on the two tensors 
        return v1 + 42

