
class Model(torch.nn.Module):
    def __init__(self, dimension):
        super().__init__()
        self.dimension  = dimension

    def forward(self, input1):
        output0 = torch.split(input1, [5], dim=self.dimension) 
        output1 = torch.cat([output0[i] for i in range(len(output0))], dim=self.dimension) 
        return output1

# Initializing the model with the `dimension` input argument set to 2
m = Model(2)

# Inputs to the model with a size of 3x4
input_data  = torch.randn(3, 4)
__output__  = m(input1=input_data)