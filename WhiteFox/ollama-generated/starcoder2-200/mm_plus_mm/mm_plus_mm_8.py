
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3, input4):
        super().__init__()
        self.mm = torch.nn.Linear(input1, 8)
 
    def forward(self, x1):
        v1 = mm(x1)
        return v1


# Initializing the model