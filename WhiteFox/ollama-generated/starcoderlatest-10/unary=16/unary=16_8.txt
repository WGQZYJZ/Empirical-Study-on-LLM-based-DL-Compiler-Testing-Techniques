
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64*64, 60) # 2D (width x height) dimensions: 64 and 64 for images are multiplied together to get 384, which is the input dimension of the first fully-connected layer.
        self.fc2 = torch.nn.Linear(60, 12)
 
    def forward(self, x):
        # The input dimensions to the two linear transformations must be equal. We can apply a linear transformation to each pixel in the input image (384), and then apply the ReLU activation function. After this stage, we are left with dimension of size 60 and depth of size 12; these dimensions correspond to the number of output classes.
        v1 = self.fc1(x.view(-1, 384)) # (64*64*4) -> 384 is the last dimension of input data x with a linear transformation.
        v2 = torch.nn.ReLU()(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 64, 64) # Batch size: 3, Number of channels in each image: 64, and number of pixels per channel in the image: 64.
