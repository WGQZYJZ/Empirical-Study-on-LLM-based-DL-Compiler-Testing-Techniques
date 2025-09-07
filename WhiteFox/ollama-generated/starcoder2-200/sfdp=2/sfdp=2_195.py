
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(3, 8)
        self.linear2  = torch.nn.Linear(3, 5)
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, torch.tensor([[0., -1., 0.], [-1., 4., -1.], [0., -1., 0.]])) + self.linear1(torch.cat((x1, x2), dim=-1)) # Apply the 3D convolution on the first input and then concatenate with the second input
        v2 = torch.nn.functional.relu(v1)  # Apply relu to the output of the convolution
        v3  = self.linear2(torch.cat((x1, x2), dim=-1)) + self.linear2(torch.cat((self.linear1(x1), self.linear1(x2)), dim=-1)) # Concatenate the linear output and the first input then concatenate with another linear output
        v4 = torch.nn.functional.relu(v3)  # Apply relu to the concatenation of the previous concatenation result 
        return torch.cat((self.linear1(torch.cat((x1, x2), dim=-1)), self.linear1(torch.cat((x1 + v4[:, :3], x2), dim=-1))), 0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 784)
x2 = torch.randn(5, 3)
 
__output_1__, __output_2__ = m(x1, x2)


