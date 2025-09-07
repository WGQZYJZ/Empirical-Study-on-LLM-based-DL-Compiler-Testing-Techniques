
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        output = self.bn(self.conv(x1))  # The batch norm layer will track running statistics of input to this convolution layer
        return output


# Initializing the model
m = Model()
torch.onnx.export(m,               # PyTorch model
                   (input_tensor),    # Inputs for the exported function
                   filename='./output',     # Output file name
                   opset_version=12      # ONNX opset version
                   )


