
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32*64, 10)
 
    def forward(self, x1):
        v1 = self.fc(x1.view(-1)) # The view operation is used to transform the input tensor from shape (1, 32 * 64) into shape (-1, 10). This transformation is necessary because a linear transformation takes an input tensor of arbitrary dimensions and produces an output tensor with fixed dimensions.
        v2 = torch.nn.functional.relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
