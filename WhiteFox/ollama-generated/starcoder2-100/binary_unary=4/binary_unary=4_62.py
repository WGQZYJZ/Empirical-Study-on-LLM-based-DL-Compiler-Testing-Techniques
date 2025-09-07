
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv2d(x1)  # Applying the linear transformation to an input tensor 
        v2 = v1 + torch.randn(*v1.shape)  # Adding another tensor to the output of the linear transformation 
        v3 = torch.relu(v2)  # Applying a ReLU activation function
        return v3

# Initializing the model
m = Model()

