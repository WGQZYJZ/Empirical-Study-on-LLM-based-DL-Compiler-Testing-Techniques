

class Model(torch.nn.Module):
    def __init__(self, tensor1=None):
        super().__init__()

        self.tensor = torch.Tensor(5) if tensor1 == None else tensor1
        print(f"self.tensor shape: {self.tensor.shape}")

        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v0  = self.tensor
        v1  = self.conv(x)
        v2  = v1 + v0

        return v2

# Initializing the model with the initial tensor 
m  = Model(input_tensor=torch.randn(5)) # Passing a random initial tensor

