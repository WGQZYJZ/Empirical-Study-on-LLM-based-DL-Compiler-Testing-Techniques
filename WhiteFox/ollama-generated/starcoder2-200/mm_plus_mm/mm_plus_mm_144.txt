
class Model(torch.nn.Module):
    def __init__(self, input1_size = 32):
        super().__init__()

        self.input1  = torch.nn.Linear(32 , 64)
        self.input2  = torch.nn.Linear(64 + 32 , 64)
        self.input3  = torch.nn.Linear(64, 5)
        
    def forward(self):

        v1  = F.relu(self.input1())  # Relu activation function of the output of the linear layer of size 32 to input1_size

        v2  = self.input2(v1 , True) # The addition of the first and second matrix multiplications.
        v2  = F.leakyrelu(self.input2()) # Leaky ReLU activation function of the output of the linear layer of size 64 to input1_size.

        v3  = self.input3() # Linear layer with the result of the addition being the input for. The result of the addition is then passed through the activation function ReLU
        return v3

# Initializing the model
m  = Model(input1_size=64)


# Inputs to the model
__input1, __input2, __input3, __input4  = torch.randn((10 , 64)), torch.randn((5, 64 )), torch.randn((5, 64 )) ,torch.randn(5)


