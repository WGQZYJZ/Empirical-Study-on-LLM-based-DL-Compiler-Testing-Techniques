
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
       v3 = torch.nn.functional.conv1d(input1, 0) # 0 is used to simulate that this convolution layer is fused with another one. 
       return v3

# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(2, 3, 4)
