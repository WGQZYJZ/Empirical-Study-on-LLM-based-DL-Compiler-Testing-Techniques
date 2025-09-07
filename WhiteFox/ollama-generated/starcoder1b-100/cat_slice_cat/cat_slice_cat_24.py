
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        output = torch.cat((x1, x2), dim=1)
        return output

 # Inputs to the model
input_tensor 1D tensor, input_tensor 1D tensor
