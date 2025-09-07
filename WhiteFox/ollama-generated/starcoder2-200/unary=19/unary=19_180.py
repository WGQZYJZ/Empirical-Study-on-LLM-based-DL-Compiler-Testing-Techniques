
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28,1)
 
    def forward(self, x):
        v1  = self.linear(x.reshape(-1,784)) #Apply a linear transformation to the input tensor with shape [batch_size, 784] and output a vector of size [batch_size]. Reshape this vector into 2d with the size 1*28 for each row.
        v2 = torch.sigmoid(v1)  #Apply the sigmoid function to the output of the linear transformation.
        return v2

# Initializing the model