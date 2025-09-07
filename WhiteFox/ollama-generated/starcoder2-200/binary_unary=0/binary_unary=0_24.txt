
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1) + m(x1) # Add the output of our model to another tensor
        v2 = v1 + other_tensor  # Add an additional constant tensor to the result
        v3 = torch.relu(v2)  # Apply ReLU activation function to the result
        return v3

# Initializing the model
m = Model()


# Inputs to the model: one is from previous model, another is ours (the model we added to the original model)
x1 = torch.randn(1, 3, 64, 64)
