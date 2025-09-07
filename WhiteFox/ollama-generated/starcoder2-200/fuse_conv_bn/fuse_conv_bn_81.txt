
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):  # Add the new input argument to the function definition 
        conv = torch.nn.Conv2d(3, 3, kernel_size=7)
        bn = torch.nn.BatchNorm2d(3)

        output = bn(conv(input))
        return output


# Initializing the model