

class Model(torch.nn.Module):
    def __init__(self, input1Size=256037, input2Size=9842):
        super().__init__()
        self.matMul = torch.nn.Linear(input1Size, 10)
        self.matMul_2 = torch.nn.Linear(input2Size, 3)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, self.matMul.weight.t())
        v2 = torch.mm(v1, self.matMul_2.weight.t())
        return v2

# Initializing the model<|end_of_code|>

m  = Model()

 # Inputs to the model<|end_of_code|>
inputSize1 = torch.randint(-9003, 67854, size=[512])
inputSize2 = torch.randint(3789, 4832, size=[4732, 9039 ])


