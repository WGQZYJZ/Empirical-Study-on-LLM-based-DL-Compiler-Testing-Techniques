
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Addition operation in the model, add a constant of 3 to the output of the convolution layer
        v3  = torch.clamp_min(v2, 0) # Clamps the result of the addition by applying the minimum clamp operator with a minimum value of 0 
        v4  = torch.clamp_max(v3, 6) # Clamps the result of the previous operation to apply the maximum clamp operator and set a maximum value of `6`
        v5  = v1 * v4 # Multiplication layer in the model that multiplies the output of the convolution by the clamped result.
        v6  = v5 / 6 # Division layer that divides the multiplication result by 6. This pattern often used for ReLU6 activations, which is a variant of the ReLU activation function that caps the maximum output value at 6.
        return v6


# Initializing and loading the model into memory on the target platform to test
m = Model()
m.load_state_dict(torch.load("path/to/model"))
m(x1)


