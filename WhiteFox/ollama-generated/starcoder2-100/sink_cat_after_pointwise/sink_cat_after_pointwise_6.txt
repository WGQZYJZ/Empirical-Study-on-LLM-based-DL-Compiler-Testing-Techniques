
class Model(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()

    def forward(self, input1, input2):  # Here we are defining 2 inputs to the model 
        output = torch.cat([input1] + list(*args), dim=...)
        output = output.view(...).relu()
        return output

# Initializing the model
m = Model()

