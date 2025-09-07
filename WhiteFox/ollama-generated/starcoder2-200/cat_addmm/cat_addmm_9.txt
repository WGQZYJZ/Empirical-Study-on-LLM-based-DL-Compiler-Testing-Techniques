
class Model(torch.nn.Module):
    def __init__(self, dim=256):
        super().__init__()
 
        self.weight1 = torch.randn(dim, 3) * (0.49 / (3 ** .5))  # Randomly initialize the weight tensor of size [dim x 3] with a Gaussian distribution that is zero mean and unit standard deviation.
        self.bias = torch.zeros([dim])  # Set the bias tensor to all zeros

    def forward(self, input):

        v1  = torch.addmm(input, self.weight1, self.bias)  # Perform matrix multiplication of the input with a randomly initialized matrix with size [dim x 3] and add it to the bias vector.
        return torch.cat([v1], dim=256)


# Initializing the model
m = Model(256)
__output__  = m(torch.randn(4, 784))