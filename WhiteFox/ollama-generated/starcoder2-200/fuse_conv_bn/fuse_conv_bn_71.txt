
class ConvBnModel(torch.nn.Module):
    def __init__(self, c=3):
        super().__init__()

        self.c  = c
        self.linear1 = torch.nn.Linear(24*c*7*7, 5)
        self.linear2 = torch.nn.Linear(64, 500)

    def forward(self, x1):
        t = x1[:, :, None] # Add 3 channels to 4d input tensor

        v = F.pad(t, (0,0,7,7)) # Pad the 5th and 6th dimensions of each 2d slice of the input tensor
        v = F.max_pool2d(v, (8,1), stride=3) # Pooling 2d tensor to 2d with max value

        v = v.reshape(-1, self.c*7*7).T @ self.linear1.weight + self.linear1.bias
        v = F.relu(v)
        v = torch.cat((v, x1), dim=0)
        v = v[..., 3:-2].T # Remove 5th and 6th dimensions

        v = v @ self.linear2.weight + self.linear2.bias 
        return F.relu(v)


# Initializing the model
m  = ConvBnModel()

# Inputs to the model, for input_tensor size (batch_size=30, height=80, width=75), 4d array with shape [height, width, channels]
x1  = torch.rand(30, 24*3, 80, 75) # The 3rd dimension of the input tensor is equal to the number of channels in the ConvBnModel class 
