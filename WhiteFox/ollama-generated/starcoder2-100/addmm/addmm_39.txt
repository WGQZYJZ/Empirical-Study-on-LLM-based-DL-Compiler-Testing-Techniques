
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, input2):
        v0 = torch.mm(input1, input2) + inp  # Adding to a constant
        return v0


# Initializing the model