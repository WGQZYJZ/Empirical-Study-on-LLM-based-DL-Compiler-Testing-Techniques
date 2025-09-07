
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute((0, 3, 1, 2)) # Permute the input tensor (this is a new line in this example). The 'permute' method of the input_tensor takes a tuple of dimenstions to permutate as argument. In this case we permute first and third dimensions
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation on the permuted tensor (this is also new). This is used as main input for the linear function which takes as arguments 3D tensor and matrix and bias vector
        return v2


# Initializing the model