
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.cat([x1, x2], dim=0)  # Concatenate the input tensors along dimension 0
        v = v.view(-1, 5 * 64)  # Reshape the concatenated tensor into a 2D matrix with shape (-1, 320).
        v = torch.nn.functional.relu(v)
        return v


# Initializing the model
m  = Model()
__output__  = m(x1=torch.randn(5), x2=torch.randn(6)) # x1 and x2 are of size 3, 4, respectively. Their concatenation results in an output tensor of shape (-1, 80)

