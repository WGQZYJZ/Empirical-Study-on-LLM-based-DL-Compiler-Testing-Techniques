 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)

    def forward(self, input_tensor1):
        output_tensor2 = self.conv(input_tensor2)
        return output_tensor1 + output_tensor2


# Initializing the model 2
m2 = Model()

# Inputs to the model 2
x3 = torch.randn(1, 4, 5) # Bias is a parameter in ConvXd and can be added when defining ConvXd
output_tensor3 = m2(x3)


