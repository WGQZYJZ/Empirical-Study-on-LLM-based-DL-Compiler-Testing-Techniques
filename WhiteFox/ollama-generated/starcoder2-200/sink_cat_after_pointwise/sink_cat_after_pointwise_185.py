
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.relu(x1)  # Apply ReLU to input tensor after it is reshaped and concatenated in a row.
        return v3

# Initializing the model
m  = Model()


