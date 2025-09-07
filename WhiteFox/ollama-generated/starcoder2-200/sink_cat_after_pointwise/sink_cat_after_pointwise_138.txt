
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        t = torch.cat([input1, input2], dim=3) # Concatenate two tensors along the 3rd dimension
        output = t[:, :, 0:4] * t[:, :, 0:-4].tanh() + \
                 t[:, :, -5:-1].relu()
        return output


# Initializing model with two inputs