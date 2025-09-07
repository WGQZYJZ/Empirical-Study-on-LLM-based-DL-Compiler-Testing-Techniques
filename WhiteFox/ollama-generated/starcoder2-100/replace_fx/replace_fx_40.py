
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Permute the input tensor and apply linear transformation to it.
        v1 = torch.nn.functional.linear(x1.permute(0, 2, 1), self.linear.weight) 
        v2 = torch.nn.functional.dropout(v1, ...) # Dropout on the result of the linear function 
        return v2

# Initializing the model
m = Model()

