
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fcs1 = torch.nn.Sequential(
            torch.nn.Linear(4, 8), # apply an affine transformation to the output of the pointwise convolution operation
            torch.nn.ReLU(),   # apply a non-linear activation function element-wise
        )
        self.fc2 = torch.nn.Linear(8, 1)    # apply an affine transformation to the output of the error function

    def forward(self, x1):
        t1 = torch.addmm(input, mat1, mat2)
        t2 = torch.cat([t1], dim)
        v1 = self.fcs1(x1) * 0.789406
        t3 = torch.relu(v1 + 1)
        v2 = t3 * 2
        v3 = self.fc2(v2)
        return v3


# Inputs to the model
x1 = torch.randn(2, 4)
