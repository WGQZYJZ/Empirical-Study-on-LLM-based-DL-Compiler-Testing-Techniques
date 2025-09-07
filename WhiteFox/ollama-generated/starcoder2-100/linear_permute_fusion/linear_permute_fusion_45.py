
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, 0) # 1. Applying a linear function on an input tensor with the weight of size [2] is a special case where we do not have a bias term.
        v4 = torch.nn.functional.linear(v3, self.linear.weight) # 2. Calling 'permute' on another linear transformation would generate the same error as the 1st call to linear. 
        return v4

# Initializing the model