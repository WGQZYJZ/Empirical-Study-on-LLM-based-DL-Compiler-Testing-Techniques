
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48*32*576, 1)

    def forward(self, x):
        v0 = x.view(-1, 9 * 32 * 48) # Flatten the input tensor to a single vector of size (9 * 32 * 48)
        v1 = self.linear(v0) # Apply a linear transformation with input and output shape of dimensionality (9 * 32 * 48), where the output has size (1). This pattern is common in neural networks, especially when working with batch images of dimensionality (batch_size x height x width x channel), and applying a final layer with an output shape (1).
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation. This is a common pattern in neural networks, especially in the final layer where the sigmoid function is used to squash the output between 0 and 1, making it interpretable as a probability.
        return v2

# Initializing the model
m = Model()

# Inputs to the model