
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.relu(x1)  # Apply ReLU to input tensor A and get the transformed version of it
        v3 = v1.permute((0, 2, 1))
        v4 = torch.bmm(v3, x2)  # Use the permuted input B as a batch multiplier on input tensor C
        return v4


# Initializing the model
m = Model()
