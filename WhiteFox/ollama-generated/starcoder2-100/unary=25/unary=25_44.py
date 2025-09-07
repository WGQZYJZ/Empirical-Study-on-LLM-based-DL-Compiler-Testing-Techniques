
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.Linear()(x1)
        v2  = (v1 > 0).float() * -0.3
        v3  = v1 * v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
input_tensor  = torch.randn(8, 4)

# Running the model with the input tensor
output  = m(input_tensor)
print("Input:\n", x1)
print("\nOutput:\n", output)

