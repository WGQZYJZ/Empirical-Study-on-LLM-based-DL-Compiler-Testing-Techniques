
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        output = torch.nn.functional.conv2d(input_tensor, self.conv1())  # Converting the conv2d to functional
        output = torch.nn.functional.batchnorm2d(output) 
        return output

# Initializing the model
m  = Model()

